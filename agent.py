import numpy as np
from collections import deque

import environment as env
import nel
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
from IPython import embed

actions = [nel.Direction.UP, nel.Direction.DOWN, nel.Direction.LEFT, nel.Direction.RIGHT]
torch.set_printoptions(precision=10)

class Policy(nn.Module):
  def __init__(self, action_dim=len(actions), state_size=30, history=2, hidden_size=16):
    super(Policy, self).__init__()
    self.fc1 = nn.Linear(state_size * history, hidden_size)
    self.fc2 = nn.Linear(hidden_size, hidden_size)
    self.fc3 = nn.Linear(hidden_size, action_dim)

  def forward(self, x):
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    return self.fc3(x)

class RLAgent(nel.Agent):
  def __init__(self, env, history=1, load_filepath=None):
    super(RLAgent, self).__init__(env.simulator, load_filepath)
    self.env = env
    self.policy = Policy()
    self.target = Policy()
    self.prev = torch.Tensor([0,0,0,0])

    for param in self.target.parameters():
      param.requires_grad = False
    # Should we have a function over the history?
    self.prev_states = deque(maxlen=history)
    self.history = history
    
  def next_move(self,epsilon=0.0):
    if(len(self.prev_states) < self.history):
      self.prev_states.append(self.create_current_frame())
      #return actions[np.random.randint(0, len(actions))]
      return np.random.choice(actions ,p=[0.5,0.1,0.2,0.2])

    random_prob = np.random.rand()
    if random_prob < epsilon:
      self.prev_states.append(self.create_current_frame())
      return np.random.choice(actions ,p=[0.5,0.1,0.2,0.2])
      #return actions[np.random.randint(0, len(actions))]

    state = self.get_state()
    context = Variable(torch.from_numpy(state), requires_grad=False)
    self.prev_states.append(self.create_current_frame())
    qs = self.policy(context)
    #print qs
    #print state
    #if torch.eq(qs.data, self.prev).all():
    #  embed()
    self.prev = qs.data
    ind = np.argmax(qs.data.numpy())
    return actions[ind]

  def create_current_frame(self):
    vis = self.vision().flatten()
    smell = self.scent()
    return np.concatenate([vis, smell])

  def get_state(self):
    if len(self.prev_states) > 0:
      context = np.concatenate(self.prev_states)
    else:
      context = np.array([])
    return np.concatenate([context, self.create_current_frame()])

  def step(self, epsilon=0.0):
    return self.env.step(self,epsilon)

  def save(self, filepath):
    pass

  def _load(self, filepath):
    pass

class RandomAgent(nel.Agent):
  def __init__(self, env, history=3, load_filepath=None):
    super(RandomAgent, self).__init__(env.simulator, load_filepath)
    self.env = env
  
  def next_move(self,epsilon=0.0):
    return np.random.choice(actions ,p=[0.5,0.1,0.2,0.2])

  def step(self):
    return self.env.step(self)
 
  def save(self, filepath):
    pass

  def _load(self, filepath):
    pass
if __name__ == '__main__':
  from config import *
  env0 = env.Environment(config1)
  agent = RLAgent(env0)
  embed()



      
    


