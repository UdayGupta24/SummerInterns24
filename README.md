
# Deep Reinforcement Learning  Project:
       
## Overview  
       
This project focuses on automating gameplay in the first-person shooter game, **Doom**. The aim is to demonstrate how automation can enhance or streamline gameplay experiences.To acheive this we have used Deep learning with reinforcement learning.We worked on intermediate tasks like FROZENLAKE,MINIGRID,TAXI-V3.
      
## Tables of contents:
     
### Environment Discussion
    
+FROZENLAKE  
+MINIGRID  
+TAXI-V3  
+DOOMS  
### Graph Plotting
    
### Tasks Given
  
### Visualizations
      
# Environment Dicussion  
1.FROZENLAKE:  
+Type: Complete Markov Process  
   +Transition probabilities are provided.  
   +Solved using Dynamic Programming since we know the complete dynamics.  
+Modes: Deterministic and Stochastic  
+State Space:  
  16 states (represented by integers: 0-15)  
+Termination Conditions:  
  +Falling into holes (5, 7, 11, 12)  
  +Reaching the Goal State (15)  
  +Reaching the maximum number of steps.  
+Actions: Left (0), Down (1), Right (2), Up (3).  
+Reward:
 0 everywhere except the Goal State, which gives 1.    
 ![Untitled video - Made with Clipchamp](https://github.com/user-attachments/assets/2e3765dc-c939-4b13-9fef-644e6caa00ba)

       
2.MINIGRID:    
 +Type: Partial Markov Process  
   +Transition probabilities are not available.  
   +Solved using Monte Carlo, SARSA, and Q-learning algorithms.  
+Mode: Deterministic  
+State Space:  
 +4x4 grid = 64 states  
 +Each block has coordinates with agent-facing directions (0, 1, 2, 3).  
+Actions:  
 Turn Anti-Clockwise (0), Turn Clockwise (1), Move Forward (2).  
+Termination Conditions:  
 +Reaching the Goal State  
 +Reaching the maximum number of steps.  
Reward:  
 0 everywhere except the Goal State, which gives 1.  
![Untitled video - Made with Clipchamp (1)](https://github.com/user-attachments/assets/1e1d7367-e516-4038-ad34-b9e2b55d89ec)  

      
3.TAXI-V3:
+Type: Fully Observable Markov Decision Process (MDP)  
  +Transition probabilities are deterministic.  
  +Solved using algorithms such as Policy Iteration, Value Iteration, Monte Carlo, SARSA, and Q-learning.  
+Mode: Deterministic  
+State Space:  
 +A 5x5 grid, resulting in 500 discrete states.  
 +State representation includes:
 +The taxi's position (row and column).  
 +Passenger's location (one of 4 possible positions or in the taxi).  
 +Destination location (one of 4 positions).  
Actions:  
6 discrete actions:  
 +Move South (0)   
 +Move North (1)   
 +Move East (2)    
 +Move West (3)   
 +Pick Up (4)   
 +Drop Off (5)    
+Termination Conditions:
  Passenger successfully delivered to the destination.  
Reward:  
  -1 for each time step (encourages efficient solutions).  
 -10 for attempting to pick up or drop off a passenger incorrectly.  
 +20 for successfully delivering the passenger to the destination.  
 ![Untitled video - Made with Clipchamp (2)](https://github.com/user-attachments/assets/c8835d68-8dea-437a-b91f-2ce1f9a9a62b)


          
4.DOOM:  
+Type: Partial Markov Process  
   +Transition probabilities are not available.  
+Mode:Deterministic  
+State Space (Observations)
  +Visual Input: The agent gets raw pixel data from the first-person view of the environment (i.e., the game screen). These are usually RGB frames (images) or grayscale.
  +Size and resolution of these frames can be controlled.
  +If multiple frames are stacked, it can form a history of states for better decision-making (similar to how humans remember past events to anticipate future outcomes).
+Action Space:  
 +Turn left  
 +Turn right 
 +Shoot  
+The rewards:  
 +-1 every moment agent is alive   
 +-5 for every bullet shot without hitting    
 +100 for shooting the monster  
![Untitled video - Made with Clipchamp (3)](https://github.com/user-attachments/assets/f95861a9-9479-4d2b-8694-05fce3d5e65c)
     
     
# GRAPH PLOTTING.
      
1. ![reward VS episodes Frozen lake deterministic](https://github.com/user-attachments/assets/2bee1deb-0971-4d3a-b8ae-d20a1c9f4c34)
   .reward VS episodes Frozen lake deterministic  
2. ![stepsize VS episode Frozen Lake deterministic](https://github.com/user-attachments/assets/dd6b24e7-5b88-4eff-bcb4-33e481f9dcf8)
   .stepsize VS episode Frozen Lake deterministic  
3. ![SARSA(backward view) reward Vs episode](https://github.com/user-attachments/assets/11a7b77b-af5f-42b8-aaea-49a0ea532dcb)
   .SARSA(backward view) Minigrid reward Vs episode  
4. ![SARSA(backward view) steps Vs episode](https://github.com/user-attachments/assets/ccfe814a-04d7-4696-81a1-c297748b4d00)
   .SARSA(backward view) Minigrid steps Vs episode  
5.![Monte Carlo reward Vs episode](https://github.com/user-attachments/assets/b3c79969-d5e5-4bce-b9d6-8aa5518c7524)
   .Monte Carlo Minigrid reward Vs episode  
6.![Monte Carlo stepsize Vs episode](https://github.com/user-attachments/assets/f3c186d6-7e6c-4e03-a8e4-7c0ef4469658)
   .Monte Carlo  Minigrid stepsize Vs episode  
7.![Q-Learning Reward Vs Episode](https://github.com/user-attachments/assets/e5204fef-4b14-46c0-8c09-5cf4f21b3b85)
   .Q-Learning Minigrid Reward Vs Episode  
8.![Q-learning Steps Vs Episode](https://github.com/user-attachments/assets/edd5739b-c6c2-4ffc-b58d-ad57f7e3f9ad)
  .Q-learning Minigrid Steps Vs Episode    
9.![SARSA reward Vs episode](https://github.com/user-attachments/assets/146c581d-d19c-41b0-be63-e3c6dd6eeab5)
 .Sarsa Minigrid Steps Vs Episode    
10.![SARSA stepVs Episode](https://github.com/user-attachments/assets/473cf61c-4704-42a8-97ae-4197743de3a5)
  .SARSA Minigrid stepVs Episode    
11.![ep_reward Vs timesteps](https://github.com/user-attachments/assets/54a3cc78-29d1-471d-9f0b-a03b7e4c343c)
  .DQN DOOM reward Vs Time steps    
12.![ep_length Vs Timesteps](https://github.com/user-attachments/assets/43a1e41b-5ccc-4508-a1b2-7218476f97a8)
  .DQN DOOM Length Vs Time steps    



 ## Project Files

| File Name                            | Description                     |
|--------------------------------------|---------------------------------|
| FrozenLake_solved_commented.py     | Solves FrozenLake environment   |
| Taxi_v3_commented.py               | Solves Taxi-v3 environment      |
| DQN code for DOOM.py               | DQN implementation for DOOM     |
| montecarlo_minigrid.py             | Monte Carlo algorithm for Minigrid |
| q-learning_minigrid.py             | Q-Learning implementation       |
| sarsa(lambda, backward_view)minigrid.py | SARSA with lambda for Minigrid |
| README.md                          | Documentation for the project   |

   
   



















