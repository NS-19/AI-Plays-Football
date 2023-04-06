import gfootball as football_env
env = football_env.create_environment(env_name='academy_empty_goal',representation='pixels',render=True)
state = env.reset()