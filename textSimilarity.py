import json
from sentence_transformers import SentenceTransformer, util

def calculate_contextual_relevance(prompt, response):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    prompt_embedding = model.encode(prompt)
    response_embedding = model.encode(response)
    
    relevance_score = util.cos_sim(prompt_embedding, response_embedding)[0][0]
    
    return {
        "relevance_score": float(relevance_score),
        "is_relevant": relevance_score > 0.5  
    }

def main():
#     prompt = "Conduct a comprehensive comparative analysis of AI performance across different computational paradigms"
#     response = """ ## Comparative Analysis of AI Performance Across Computational Paradigms

# Artificial Intelligence (AI) is rapidly evolving, pushing the boundaries of what's possible.  The choice of an appropriate computational paradigm significantly impacts AI performance in various aspects: efficiency, scalability, and accuracy. 

# This analysis explores the strengths and weaknesses of **different paradigms:**

# **1. Central Processing Unit (CPU)-based Approach:**
# * **Description:** Traditional approach using general-purpose CPUs for calculations and processing data.  
# * **Advantages:** 
#     * Mature technology with extensive libraries & tools.
#     * Relatively low cost, easy to implement and maintain.
#     * Widely available hardware support.
# * **Disadvantages:** 
#     * Limited scalability for massive datasets.
#     * Often slower than specialized hardware for AI tasks. 
#     * Computationally intensive for complex models like GANs or RNNs.

# **2. Graphics Processing Unit (GPU)-based Approach:**
# * **Description:** Special-purpose processors designed for parallel processing and handling large datasets.  
# * **Advantages:** 
#     * Significantly faster for matrix multiplication, convolution operations critical in deep learning.
#     * High parallel processing capabilities, ideal for massive datasets.
#     * Allows training of larger models and complex architectures.
# * **Disadvantages:** 
#     * Higher cost than CPUs.
#     * Requires specialized software & frameworks like CUDA or OpenCL. 

# **3. Field-Programmable Gate Arrays (FPGAs):**
# * **Description:** Hardware circuits customizable at the design level for specific AI tasks.  
# * **Advantages:** 
#     * Exceptional customizability and performance optimization.
#     * Highly efficient for computationally complex tasks with high throughput.
#     * Ability to accelerate specific algorithms, leading to significant speed-ups. 
# * **Disadvantages:** 
#     * Complex development process requiring specialized skills & knowledge.
#     * Initial setup is costly & time-consuming.
#     * Hardware limited by chip size and power constraints.

# **4. Quantum Computing:**
# * **Description:** Exploiting quantum mechanics principles for advanced computation capabilities. 
# * **Advantages:** 
#     * Potential to solve problems that are intractable for classical computers, like complex simulations or optimization tasks.
#     * Fast processing for certain types of AI algorithms, such as reinforcement learning and quantum machine learning.
# * **Disadvantages:** 
#     * Limited scalability and availability at present.
#     * Requires extensive development effort to overcome technical challenges.
#     * High cost & complexity in building and maintaining quantum computers.

# **5. Neuromorphic Computing (e.g., Loihi chips):**
# * **Description:** Mimics the human brain's structure for efficient processing of real-time sensory information. 
# * **Advantages:** 
#     * Reduced power consumption compared to traditional computing.
#     * Potential for faster learning and adaptation, leading to more responsive AI systems.  
# * **Disadvantages:** 
#     * Limited application scope currently.
#     * Requires specialized hardware and software development with ongoing research in this domain.

# **Specific Examples of AI Performance Across Paradigms:**


# | Paradigm | Applications | Advantages | Disadvantages | Performance Impact |
# |---|---|---|---|---|
# | **CPU-based** | Image recognition, text classification, basic machine learning algorithms | Mature technology, wide accessibility | Limited for large datasets and complex models; slower performance | Less efficient for computationally demanding tasks |
# | **GPU-based** | Deep learning, computer vision, natural language processing | High speed with matrix operations; suitable for massive datasets | Requires specialized hardware & software; less scalable than FPGA | Faster training of deep learning models |
# | **FPGA-based** | Scientific simulations, real-time applications, custom algorithms | Highly customizable and optimized; faster performance for specific tasks | Complex development process; limited scalability |  Increased efficiency for complex algorithms |
# | **Quantum Computing** | Drug discovery, optimization problems, new material design | Solving previously intractable problems in AI | Still in its early stage with high cost and limitations | Potentially groundbreaking breakthroughs in AI |
# | **Neuromorphic Computing (Loihi) | Adaptive learning, efficient sensory processing | Lower power consumption; faster learning | Limited to specific applications; evolving technology | Enhanced efficiency for real-time applications |

#  **Conclusion:**


# The choice of computational paradigm depends on the specific application and its requirements.  For data-intensive AI tasks like deep learning, GPUs are increasingly favored for their scalability and speed, while FPGAs excel in optimizing complex algorithms for specialized purposes. As AI technology progresses, new paradigms like quantum computing and neuromorphic circuits hold promising potential for accelerating future advancements in this field. 


# **Further Considerations:**


# * **Data availability and preprocessing**: The size and complexity of data significantly impact performance across all paradigms.
# * **Model architecture & complexity**:  The design of the AI model will influence performance based on the chosen paradigm.
# * **Ongoing research and development**: Continuous advancement in hardware, software, and algorithms drives efficiency and scalability for each paradigm. 


# By understanding these different aspects and analyzing their strengths and weaknesses, researchers and developers can choose the most suitable computational approach to achieve optimal AI performance for diverse applications.

#  """
    with open("data/test.txt", "r") as file:
        data = json.load(file)
        prompt = data["prompt"]

    with open("data/output.txt", "r") as file:
        response = file.readlines()

    relevance_result = calculate_contextual_relevance(prompt, response)
    
    print("Prompt:", prompt)
    print("Response:", response)
    print("Relevance Score:", relevance_result['relevance_score'])
    print("Is Relevant:", relevance_result['is_relevant'])

if __name__ == "__main__":
    main()
