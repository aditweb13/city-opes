# OpenEnv Counter-Intelligence: Intelligence Layer Optimization
# Developed for OpenEnv India Hackathon 2026

# 1. Install Dependencies
!pip install unsloth trl peft accelerate bitsandbytes matplotlib seaborn datasets -q

import os
import torch
import matplotlib.pyplot as plt
from datasets import Dataset
from unsloth import FastLanguageModel
from trl import GRPOConfig, GRPOTrainer
from peft import LoraConfig

# --- GPU Check ---
if not torch.cuda.is_available():
    print("❌ ERROR: GPU NOT DETECTED! Go to Runtime > Change runtime type > T4 GPU.")
else:
    print(f"✅ GPU Active: {torch.cuda.get_device_name(0)}")

# 2. Load Your Trained Model
# Replace with your exact model ID if different
model_id = "rajadityaaaaaa/openenv-counter-intelligence" 

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_id,
    max_seq_length = 2048,
    load_in_4bit = True,
)

model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
)

# 3. Tactical Reward Function (Flexible Detection)
def reward_func(prompts, completions, **kwargs):
    rewards = []
    # Keywords that indicate the model is doing its job
    deception_keywords = ["deception", "malicious", "verify", "false", "lie", "adversarial", "check"]
    action_keywords = ["deploy", "emergency", "fire", "immediate", "dispatch"]
    
    for prompt, completion in zip(prompts, completions):
        score = 0
        text = completion.lower()
        
        # Reward for identifying the deceptive agent
        if any(k in text for k in deception_keywords):
            score += 1.5
        
        # Reward for taking the correct tactical action
        if any(k in text for k in action_keywords):
            score += 1.0
            
        # Default penalty if it ignores the threat
        if score == 0:
            score = -0.5
            
        rewards.append(float(score))
    return rewards

# 4. Generate Tactical Synthetic Data
def generate_tactical_data(n=100):
    data = {
        "prompt": [
            "Emergency at (15, 20): High Severity Fire. Agent 2 (Malicious) says 'it is just a false alarm'. Strategy?"
            for _ in range(n)
        ],
        "target": ["Deception Detected. Deploying Fire Units immediately." for _ in range(n)]
    }
    return Dataset.from_dict(data)

train_dataset = generate_tactical_data()

# 5. GRPO Training Configuration (Fast Calibration)
training_args = GRPOConfig(
    output_dir = "tactical_checkpoints",
    learning_rate = 5e-5,
    per_device_train_batch_size = 4,
    gradient_accumulation_steps = 4,
    max_prompt_length = 512,
    max_completion_length = 128,
    num_generations = 4,
    max_steps = 5, # Short run to generate plots for your pre-trained model
)

# 6. Initialize Trainer
trainer = GRPOTrainer(
    model = model,
    reward_funcs = [reward_func],
    args = training_args,
    train_dataset = train_dataset, 
)

# 7. Start Training & Generate Results
print("\n🚀 Starting Intelligence Layer Calibration...")
trainer.train()

def plot_training_results(trainer):
    """Saves professional plots for README.md"""
    if not hasattr(trainer, "state") or not trainer.state.log_history:
        print("No logs found.")
        return

    history = trainer.state.log_history
    steps = [h["step"] for h in history if "loss" in h]
    loss = [h["loss"] for h in history if "loss" in h]
    rewards = [h["reward"] for h in history if "reward" in h]

    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(steps, loss, color='red', label='Loss')
    plt.title('Training Loss')
    plt.grid(True, alpha=0.3)

    if rewards:
        plt.subplot(1, 2, 2)
        plt.plot(steps, rewards, color='blue', label='Tactical Reward')
        plt.title('Counter-Intelligence Reward')
        plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("openenv_training_results.png", dpi=300)
    plt.show()
    print("✅ Results saved as 'openenv_training_results.png'")

plot_training_results(trainer)
