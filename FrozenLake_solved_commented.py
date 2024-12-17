# Importing necessary libraries
import gym
# Importing necessary libraries
import numpy as np
# Importing necessary libraries
import time



# Function to compute the value function for a given policy
def value_function(currvaluefunction,prevvaluefunction,nS,nA,policy,P,gamma=.9,tol=1e-3):
   maxi=float('inf')
   while(maxi>(tol)):
       for s in range(nS):
           sum1=0
           action=policy[s]
           for prob,nextstate,reward,_ in P[s][action]:
               sum1=sum1+prob*(reward+gamma*prevvaluefunction[nextstate])
           currvaluefunction[s]=sum1
       maxi=np.max(np.abs(currvaluefunction - prevvaluefunction))
       for s in range(nS):
           prevvaluefunction[s]=currvaluefunction[s]
   return currvaluefunction
              

# Function to evaluate a policy using the value function
def policy_evaluation(currvaluefunction,prevvaluefunction,nS,nA,policy,P,gamma):
    evaluated_function= value_function(currvaluefunction,prevvaluefunction,nS,nA,policy,P,gamma=.9)
    return evaluated_function



# Function to improve a policy by finding the optimal action for each state
def policy_improvement(currvaluefunction,nA,nS,policy,P,gamma=.9):
    new_policy=np.zeros(nS)
    for s in range(nS):
        q={}
        for i in range(nA):
            for prob,nextstate,reward,_ in P[s][i]:
                q[i]=prob*(reward+gamma*currvaluefunction[nextstate])
        q=sorted(q.items(),key=lambda item:item[1],reverse=True)
        optimised_action=q[0][0]
        new_policy[s]=optimised_action
    return new_policy



# Function to perform policy iteration to find the optimal policy
def policy_iteration(P,nS,nA,gamma=.9,tol=1e-3):
    currvaluefunction=np.zeros(nS)
    prevvaluefunction=np.zeros(nS)
    policy=np.array([0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3])
    valuefunction=policy_evaluation(currvaluefunction,prevvaluefunction,nS,nA,policy,P,gamma=.9)
    newpolicy=policy_improvement(valuefunction,nA,nS,policy,P,gamma=.9)
    while not np.array_equal(newpolicy,policy):
        policy = newpolicy.copy()
        valuefunction=policy_evaluation(currvaluefunction,prevvaluefunction,nS,nA,policy,P,gamma=.9)
        newpolicy=policy_improvement(valuefunction,nA,nS,policy,P,gamma=.9)
    return valuefunction,newpolicy



# Function to perform value iteration to find the optimal policy and value function
def value_iteration(P,nA,nS,gamma=.9,tol=1e-3):
    currvaluefunction=np.zeros(nS)
    prevvaluefunction=np.zeros(nS)
    policy=np.array([0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3])
    for s in range(nS):
        sum1=0
        action=policy[s]
        for prob,nextstate,reward,_ in P[s][action]:
            sum1=sum1+prob*(reward+gamma*prevvaluefunction[nextstate])
        currvaluefunction[s]=sum1
    prevvaluefunction=currvaluefunction.copy()
    maxi=float('inf')
    while(maxi>(tol)):
        for s in range(nS):
            q=[]
            for i in range(nA):
                for prob,nextstate,reward,_ in P[s][i]:
                    q.append(prob*(reward+gamma*prevvaluefunction[nextstate]))
            q.sort(reverse=True)
            currvaluefunction[s]=q[0]
        maxi=np.max(np.abs(currvaluefunction - prevvaluefunction))
        for s in range(nS):
            prevvaluefunction[s]= currvaluefunction[s]
    new_policy=np.zeros(nS)
    for s in range(nS):
        q={}
        for i in range(nA):
            for prob,nextstate,reward,_ in P[s][i]:
                q[i]=prob*(reward+gamma*currvaluefunction[nextstate])
        q=sorted(q.items(),key=lambda item:item[1],reverse=True)
        optimised_action=q[0][0]
        new_policy[s]=optimised_action
    return currvaluefunction,new_policy



# Function to render a single episode using a given policy
def render_single(env, policy, max_steps=100):
    episode_reward = 0
    #############
    ob = env.reset()[0]
    #############
    for t in range(max_steps):
        env.render()
        time.sleep(0.25)
        ##############
        a = int(policy[ob])
        ##############
        step_result = env.step(a)
        if len(step_result) == 4:
            ob, rew, done, info = step_result
        else:
            ob, rew, done, truncated, info = step_result
        ##############
        episode_reward += rew
        if done:
            break
    env.render()
    if not done:
        print("The agent didn't reach a terminal state in {} steps.".format(max_steps))
    else:
        print("Episode reward: %f" % episode_reward)


# Main execution block to run the FrozenLake environment and apply policy/value iteration
if __name__ == "__main__":

    # Specify the environment name and initialize environment variables
    name="FrozenLake-v1"

    # Transition probabilities and rewards for each state-action pair
    P= {0: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 4, 0.0, False)], 2: [(1.0, 1, 0.0, False)], 3: [(1.0, 0, 0.0, False)]}, 1: {0: [(1.0, 0, 0.0, False)], 1: [(1.0, 5, 0.0, True)], 2: [(1.0, 2, 0.0, False)], 3: [(1.0, 1, 0.0, False)]}, 2: {0: [(1.0, 1, 0.0, False)], 1: [(1.0, 6, 0.0, False)], 2: [(1.0, 3, 0.0, False)], 3: [(1.0, 2, 0.0, False)]}, 3: {0: [(1.0, 2, 0.0, False)], 1: [(1.0, 7, 0.0, True)], 2: [(1.0, 3, 0.0, False)], 3: [(1.0, 3, 0.0, False)]}, 4: {0: [(1.0, 4, 0.0, False)], 1: [(1.0, 8, 0.0, False)], 2: [(1.0, 5, 0.0, True)], 3: [(1.0, 0, 0.0, False)]}, 5: {0: [(1.0, 5, 0, True)], 1: [(1.0, 5, 0, True)], 2: [(1.0, 5, 0, True)], 3: [(1.0, 5, 0, True)]}, 6: {0: [(1.0, 5, 0.0, True)], 1: [(1.0, 10, 0.0, False)], 2: [(1.0, 7, 0.0, True)], 3: [(1.0, 2, 0.0, False)]}, 7: {0: [(1.0, 7, 0, True)], 1: [(1.0, 7, 0, True)], 2: [(1.0, 7, 0, True)], 3: [(1.0, 7, 0, True)]}, 8: {0: [(1.0, 8, 0.0, False)], 1: [(1.0, 12, 0.0, True)], 2: [(1.0, 9, 0.0, False)], 3: [(1.0, 4, 0.0, False)]}, 9: {0: [(1.0, 8, 0.0, False)], 1: [(1.0, 13, 0.0, False)], 2: [(1.0, 10, 0.0, False)], 3: [(1.0, 5, 0.0, True)]}, 10: {0: [(1.0, 9, 0.0, False)], 1: [(1.0, 14, 0.0, False)], 2: [(1.0, 11, 0.0, True)], 3: [(1.0, 6, 0.0, False)]}, 11: {0: [(1.0, 11, 0, True)], 1: [(1.0, 11, 0, True)], 2: [(1.0, 11, 0, True)], 3: [(1.0, 11, 0, True)]}, 12: {0: [(1.0, 12, 0, True)], 1: [(1.0, 12, 0, True)], 2: [(1.0, 12, 0, True)], 3: [(1.0, 12, 0, True)]}, 13: {0: [(1.0, 12, 0.0, True)], 1: [(1.0, 13, 0.0, False)], 2: [(1.0, 14, 0.0, False)], 3: [(1.0, 9, 0.0, False)]}, 14: {0: [(1.0, 13, 0.0, False)], 1: [(1.0, 14, 0.0, False)], 2: [(1.0, 15, 1.0, True)], 3: [(1.0, 10, 0.0, False)]}, 15: {0: [(1.0, 15, 0, True)], 1: [(1.0, 15, 0, True)], 2: [(1.0, 15, 0, True)], 3: [(1.0, 15, 0, True)]}}
    nS=16
    nA=4
    env=gym.make(name,is_slippery=False,render_mode="human")
    

    # Print section headers for clarity
    print("\n" + "-" * 25 + "\nBeginning Policy Iteration\n" + "-" * 25)

    # Perform policy iteration and render the optimal policy
    V_pi,P_pi=policy_iteration(P,nS,nA,gamma=.9,tol=1e-3)
    render_single(env,P_pi,100)
    

    # Print section headers for clarity
    print("\n" + "-" * 25 + "\nBeginning value Iteration\n" + "-" * 25)

    # Perform value iteration and render the optimal policy
    V_vi,P_vi=value_iteration(P,nA,nS,gamma=.9,tol=1e-3)
    render_single(env,P_vi,100)
    
 

