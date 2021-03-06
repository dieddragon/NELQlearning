import sys
sys.path.append("../nel_framework/nel/")
import nel

#---------------- config 1
items1 = []
items1.append(nel.Item("banana", [1.0, 1.0, 0.0], [1.0, 1.0, 0.0], True))

intensity_fn_args1 = [-2.0]
interaction_fn_args1 = [len(items1)]
interaction_fn_args1.extend([40.0, 200.0, 0.0, -40.0]) # parameters for interaction between item 0 and item 0

config1 = nel.SimulatorConfig(max_steps_per_movement=1, vision_range=1,
  patch_size=32, gibbs_num_iter=10, items=items1, agent_color=[0.0, 0.0, 1.0],
  collision_policy=nel.MovementConflictPolicy.FIRST_COME_FIRST_SERVED,
  decay_param=0.4, diffusion_param=0.14, deleted_item_lifetime=2000,
  intensity_fn=nel.IntensityFunction.CONSTANT, intensity_fn_args=intensity_fn_args1,
  interaction_fn=nel.InteractionFunction.PIECEWISE_BOX, interaction_fn_args=interaction_fn_args1)

items = []
items.append(nel.Item("banana", [0.0, 1.0, 0.0], [0.0, 1.0, 0.0], False))
items.append(nel.Item("onion", [1.0, 0.0, 0.0], [1.0, 0.0, 0.0], False))
items.append(nel.Item("jellybean", [0.0, 0.0, 1.0], [0.0, 0.0, 1.0], True))

intensity_fn_args = [-5.3, -5.0, -5.3]
interaction_fn_args = [len(items)]
interaction_fn_args.extend([10.0, 200.0, 0.0, -6.0])     # parameters for interaction between item 0 and item 0
interaction_fn_args.extend([200.0, 0.0, -6.0, -6.0])     # parameters for interaction between item 0 and item 1
interaction_fn_args.extend([10.0, 200.0, 2.0, -100.0])   # parameters for interaction between item 0 and item 2
interaction_fn_args.extend([200.0, 0.0, -6.0, -6.0])     # parameters for interaction between item 1 and item 0
interaction_fn_args.extend([0.0, 0.0, 0.0, 0.0])         # parameters for interaction between item 1 and item 1
interaction_fn_args.extend([200.0, 0.0, -100.0, -100.0]) # parameters for interaction between item 1 and item 2
interaction_fn_args.extend([10.0, 200.0, 2.0, -100.0])   # parameters for interaction between item 2 and item 0
interaction_fn_args.extend([200.0, 0.0, -100.0, -100.0]) # parameters for interaction between item 2 and item 1
interaction_fn_args.extend([10.0, 200.0, 0.0, -6.0])     # parameters for interaction between item 2 and item 2

config2 = nel.SimulatorConfig(max_steps_per_movement=1, vision_range=1,
	patch_size=32, gibbs_num_iter=10, items=items, agent_color=[0.0, 0.0, 1.0],
	collision_policy=nel.MovementConflictPolicy.FIRST_COME_FIRST_SERVED,
	decay_param=0.4, diffusion_param=0.14, deleted_item_lifetime=2000,
	intensity_fn=nel.IntensityFunction.CONSTANT, intensity_fn_args=intensity_fn_args,
	interaction_fn=nel.InteractionFunction.PIECEWISE_BOX, interaction_fn_args=interaction_fn_args)
