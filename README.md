<h1 align="center">
  <img src="assets/ai.png" width="48" alt="Awesome Embodied Agents icon">
  Awesome Embodied Agents
</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
</p>

A curated list of papers and resources on VLM/LLM-based embodied agents, focusing on memory, reasoning, planning, exploration, navigation, manipulation, and evaluation.

<!--
## Scope

This repository focuses on embodied AI systems where VLMs or MLLMs serve as agentic components: perceiving the environment, maintaining memory, reasoning over space and time, planning actions, interacting with tools or skills, and adapting through feedback.

Included:

- Embodied memory and embodied RAG
- VLM/MLLM-based embodied reasoning and planning
- Embodied exploration and navigation agents
- Embodied question answering
- Manipulation agents using VLMs as planners, skill selectors, or high-level controllers
- Benchmarks and evaluation resources for embodied agents

Usually out of scope:

- End-to-end VLA policies
- World models or video prediction models
- Low-level robot control
- Diffusion policies
- Generic LLM agents without embodied perception

Borderline works are included when the VLM/MLLM is used as an agentic decision-making, memory, reasoning, or planning module rather than only as a frozen encoder or direct action policy.
-->

## Table of Contents

| Category | Description |
| :--- | :--- |
| [Survey](#survey) | Overviews, taxonomies, and perspective papers |
| [Benchmark](#benchmark) | Evaluation suites for embodied agent capabilities |
| [Agent System](#agent-system) | Integrated embodied agent systems and platforms |
| [Memory](#memory) | Spatial, episodic, and retrieval-augmented memory |
| [Reasoning & Planning](#reasoning--planning) | Task planning, reflection, replanning, and governance |
| [Active](#active) | Active perception, exploration, and spatial belief construction |
| [Navigation](#navigation) | Object-goal, semantic, and vision-language navigation |
| [EQA](#eqa) | Embodied question answering with memory and exploration |
| [Manipulation](#manipulation) | VLM/LLM-guided robotic manipulation agents |
| [Related Lists](#related-lists) | Adjacent curated lists and resources |

> **Paper Ordering** - Papers are sorted by year in descending order within each section. Within the same year, representative works may be highlighted first.

> **Contributing** - This repository is continuously updated. If you have papers, projects, or resources not yet included, please submit a Pull Request or open an Issue.

## Survey

* [2026] Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses [[paper](https://arxiv.org/pdf/2605.02900)]
* [2026] Self-evolving Embodied AI [[paper](https://arxiv.org/pdf/2602.04411)]
* [2026] Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges [[paper](https://arxiv.org/pdf/2601.02377)]
* [2025] Multimodal Data Storage and Retrieval for Embodied AI: A Survey [[paper](https://arxiv.org/pdf/2508.13901)]
* [2025] Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey [[paper](https://arxiv.org/pdf/2508.13073)] [[project](https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation)]
* [2025] Large Model Empowered Embodied AI: A Survey on Decision-Making and Embodied Learning [[paper](https://arxiv.org/pdf/2508.10399)]
* [2025] Foundation Model Driven Robotics: A Comprehensive Review [[paper](https://arxiv.org/pdf/2507.10087)]
* [2025] Embodied AI Agents: Modeling the World [[paper](https://arxiv.org/pdf/2506.22355)]
* [2025] Neural Brain: A Neuroscience-inspired Framework for Embodied Agents [[paper](https://arxiv.org/pdf/2505.07634)] [[project](https://github.com/EmPACTLab/Neural-Brain-for-Embodied-Agents)]
* [2025] A Survey of Robotic Navigation and Manipulation with Physics Simulators in the Era of Embodied AI [[paper](https://arxiv.org/pdf/2505.01458)]
* [2025] Multimodal Perception for Goal-oriented Navigation: A Survey [[paper](https://arxiv.org/pdf/2504.15643)]
* [2025] Exploring Embodied Multimodal Large Models: Development, Datasets, and Future Directions [[paper](https://arxiv.org/pdf/2502.15336)]
* [2024] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI [[paper](https://arxiv.org/pdf/2407.06886)]
* [2023] Foundation Models in Robotics: Applications, Challenges, and the Future [[paper](https://arxiv.org/pdf/2312.07843)] [[project](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models)]
* [2023] Large Language Models for Robotics: A Survey [[paper](https://arxiv.org/pdf/2311.07226)]
* [2021] Vision-Language Navigation: A Survey and Taxonomy [[paper](https://arxiv.org/pdf/2108.11544)]
* [2021] A Survey of Embodied AI: From Simulators to Research Tasks [[paper](https://arxiv.org/pdf/2103.04918)]

## Benchmark

* [2026] ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop [[paper](https://arxiv.org/pdf/2605.18746)] [[project](https://esi-bench.github.io/)]
* [2026] RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark [[paper](https://arxiv.org/pdf/2605.10921)] [[project](https://robomemarena.github.io/)]
* [2026] Done, But Not Sure: Disentangling World Completion from Self-Termination in Embodied Agents [[paper](https://arxiv.org/pdf/2605.08747)]
* [2026] SpaMEM: Benchmarking Dynamic Spatial Reasoning via Perception-Memory Integration in Embodied Environments [[paper](https://arxiv.org/pdf/2604.22409)]
* [2026] E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes [[paper](https://arxiv.org/pdf/2604.17969)]
* [2026] CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation [[paper](https://arxiv.org/pdf/2603.22435)] [[project](https://capgym.github.io/)]
* [2026] NavTrust: Benchmarking Trustworthiness for Embodied Navigation [[paper](https://arxiv.org/pdf/2603.19229)] [[project](https://navtrust.github.io/)]
* [2026] AsgardBench: Evaluating Visually Grounded Interactive Planning Under Minimal Feedback [[paper](https://arxiv.org/pdf/2603.15888)]
* [2026] RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies [[paper](https://arxiv.org/pdf/2603.04639)] [[project](https://robomme.github.io/)] [[code](https://github.com/RoboMME/robomme_benchmark)]
* [2026] RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design [[paper](https://arxiv.org/pdf/2603.01229)] [[project](https://rmbench.github.io/)]
* [2026] How Foundational Skills Influence VLM-based Embodied Agents: A Native Perspective [[paper](https://arxiv.org/pdf/2602.20687)]
* [2025] CFG-Bench: Beyond Description: Cognitively Benchmarking Fine-Grained Action for Embodied Agents [[paper](https://arxiv.org/pdf/2511.18685)]
* [2025] Ego3D-Bench: Spatial Reasoning with Vision-Language Models in Ego-Centric Multi-View Scenes [[paper](https://arxiv.org/pdf/2509.06266)] [[project](https://vbdi.github.io/Ego3D-Bench-webpage/)]
* [2025] AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions [[paper](https://arxiv.org/pdf/2506.14697)]
* [2025] FindingDory: A Benchmark to Evaluate Memory in Embodied Agents [[paper](https://arxiv.org/pdf/2506.15635)] [[project](https://findingdory-benchmark.github.io/)]
* [2025] SD-OVON: A Semantics-aware Dataset and Benchmark Generation Pipeline for Open-Vocabulary Object Navigation in Dynamic Scenes [[paper](https://arxiv.org/pdf/2505.18881)]
* [2025] ManipBench: Benchmarking Vision-Language Models for Low-Level Robot Manipulation [[paper](https://arxiv.org/pdf/2505.09698)] [[project](https://manipbench.github.io/)]
* [2025] EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents [[paper](https://arxiv.org/pdf/2502.09560)] [[project](https://embodiedbench.github.io/)] [[code](https://github.com/EmbodiedBench/EmbodiedBench)]
* [2024] ET-Plan-Bench: Embodied Task-level Planning Benchmark Towards Spatial-Temporal Cognition with Foundation Models [[paper](https://arxiv.org/pdf/2410.14682)]
* [2024] HM3D-OVON: A Dataset and Benchmark for Open-Vocabulary Object Goal Navigation [[paper](https://arxiv.org/pdf/2409.14296)] [[project](https://naoki.io/ovon)]
* [2024] EmbSpatial-Bench: Benchmarking Spatial Understanding for Embodied Tasks with Large Vision-Language Models [[paper](https://arxiv.org/pdf/2406.05756)]
* [2024] GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation [[paper](https://arxiv.org/pdf/2404.06609)] [[project](https://mukulkhanna.github.io/goat-bench/)]
* [2022] Instance-Specific Image Goal Navigation: Training Embodied Agents to Find Object Instances [[paper](https://arxiv.org/pdf/2211.15876)]
* [2020] Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding [[paper](https://arxiv.org/pdf/2010.07954)]
* [2020] ObjectNav Revisited: On Evaluation of Embodied Agents Navigating to Objects [[paper](https://arxiv.org/pdf/2006.13171)]

## Agent System

* [2026] SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing [[paper](https://arxiv.org/pdf/2604.14399)] [[code](https://github.com/wuaodi/SpaceMind)]
* [2026] ABot-Claw: A Foundation for Persistent, Cooperative, and Self-Evolving Robotic Agents [[paper](https://arxiv.org/pdf/2604.10096)]
* [2026] RoboAgent: Chaining Basic Capabilities for Embodied Task Planning [[paper](https://arxiv.org/pdf/2604.07774)] [[code](https://github.com/woyut/RoboAgent_CVPR26)]
* [2026] RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks [[paper](https://arxiv.org/pdf/2603.11558)]
* [2026] AgenticLab: A Real-World Robot Agent Platform that Can See, Think, and Act [[paper](https://arxiv.org/pdf/2602.01662)]
* [2025] RoboBrain 2.0 Technical Report [[paper](https://arxiv.org/pdf/2507.02029)] [[project](https://superrobobrain.github.io/)]
* [2025] Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents [[paper](https://arxiv.org/pdf/2505.23450)] [[project](https://agentic-robot.github.io/)]
* [2025] RoboOS: A Hierarchical Embodied Framework for Cross-Embodiment and Multi-Agent Collaboration [[paper](https://arxiv.org/pdf/2505.03673)] [[code](https://github.com/FlagOpen/RoboOS)]
* [2025] RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete [[paper](https://arxiv.org/pdf/2502.21257)] [[project](https://superrobobrain.github.io/)]
* [2024] BUMBLE: Unifying Reasoning and Acting with Vision-Language Models for Building-Wide Mobile Manipulation [[paper](https://arxiv.org/pdf/2410.06237)] [[project](https://robin-lab.cs.utexas.edu/BUMBLE/)]
* [2024] Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks [[paper](https://arxiv.org/pdf/2408.03615)] [[project](https://cybertronagent.github.io/Optimus-1.github.io/)] [[code](https://github.com/JiuTian-VL/Optimus-1)]
* [2024] OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics [[paper](https://arxiv.org/pdf/2401.12202)] [[project](https://ok-robot.github.io/)]
* [2023] JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models [[paper](https://arxiv.org/pdf/2311.05997)] [[project](https://craftjarvis.org/JARVIS-1)]
* [2023] Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models [[paper](https://arxiv.org/pdf/2310.15127)] [[project](https://helper-agent-llm.github.io/)]
* [2023] Voyager: An Open-Ended Embodied Agent with Large Language Models [[paper](https://arxiv.org/pdf/2305.16291)] [[project](https://voyager.minedojo.org/)] [[code](https://github.com/MineDojo/Voyager)]

## Memory

* [2026] Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction [[paper](https://arxiv.org/pdf/2605.18729)] [[project](https://robocortex66.github.io/robo-cortex/)]
* [2026] BrainMem: Brain-Inspired Evolving Memory for Embodied Agent Task Planning [[paper](https://arxiv.org/pdf/2604.16331)]
* [2026] EmbodiedLGR: Integrating Lightweight Graph Representation and Retrieval for Semantic-Spatial Memory in Robotic Agents [[paper](https://arxiv.org/pdf/2604.18271)]
* [2026] HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System [[paper](https://arxiv.org/pdf/2603.14807)] [[code](https://github.com/lvkailin0118/HiMemVLN)]
* [2026] CMMR-VLN: Vision-and-Language Navigation via Continual Multimodal Memory Retrieval [[paper](https://arxiv.org/pdf/2603.07997)]
* [2026] MEM: Multi-Scale Embodied Memory for Vision Language Action Models [[paper](https://arxiv.org/pdf/2603.03596)] [[project](https://www.pi.website/research/memory)]
* [2026] PhysMem: Scaling Test-Time Memory for Embodied Physical Reasoning [[paper](https://arxiv.org/pdf/2602.20323)] [[project](https://phys-mem.github.io/)]
* [2026] HIMM: Human-Inspired Long-Term Memory Modeling for Embodied Exploration and Question Answering [[paper](https://arxiv.org/pdf/2602.15513)]
* [2026] MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents [[paper](https://arxiv.org/pdf/2601.20831)]
* [2026] SpatialMem: Unified 3D Memory with Metric Anchoring and Fast Retrieval [[paper](https://arxiv.org/pdf/2601.14895)]
* [2026] Planning with an Embodied Learnable Memory [[paper](https://openreview.net/pdf?id=79BOATBal9)]
* [2025] MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning [[paper](https://arxiv.org/pdf/2512.16909)] [[project](https://hybridrobotics.github.io/MomaGraph/)]
* [2025] JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation [[paper](https://arxiv.org/pdf/2509.22548)] [[project](https://miv-xjtu.github.io/JanusVLN.github.io/)]
* [2025] MSNav: Zero-Shot Vision-and-Language Navigation with Dynamic Memory and LLM Spatial Reasoning [[paper](https://arxiv.org/pdf/2508.16654)]
* [2025] Open Scene Graphs for Open-World Object-Goal Navigation [[paper](https://arxiv.org/pdf/2508.04678)] [[project](https://open-scene-graphs.github.io/)]
* [2025] Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory [[paper](https://arxiv.org/pdf/2508.09736)] [[code](https://github.com/bytedance-seed/m3-agent)]
* [2025] RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Lifelong Learning in Physical Embodied Systems [[paper](https://arxiv.org/pdf/2508.01415)]
* [2025] GraphPad: Inference-Time 3D Scene Graph Updates for Embodied Question Answering [[paper](https://arxiv.org/pdf/2506.01174)]
* [2025] 3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model [[paper](https://arxiv.org/pdf/2505.22657)] [[project](https://3dllm-mem.github.io/)]
* [2025] Open-Vocabulary Functional 3D Scene Graphs for Real-World Indoor Spaces [[paper](https://arxiv.org/pdf/2503.19199)] [[project](https://openfungraph.github.io/)]
* [2025] MapNav: A Novel Memory Representation via Annotated Semantic Maps for VLM-based Vision-and-Language Navigation [[paper](https://arxiv.org/pdf/2502.13451)]
* [2025] STMA: A Spatio-Temporal Memory Agent for Long-Horizon Embodied Task Planning [[paper](https://arxiv.org/pdf/2502.10177)]
* [2025] Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding [[paper](https://arxiv.org/pdf/2501.00358)] [[project](https://embodied-videoagent.github.io/)]
* [2025] Planning from Imagination: Episodic Simulation and Episodic Memory for Vision-and-Language Navigation [[paper](https://arxiv.org/pdf/2412.01857)]
* [2024] 3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning [[paper](https://arxiv.org/pdf/2411.17735)] [[project](https://umass-embodied-agi.github.io/3D-Mem/)] [[code](https://github.com/UMass-Embodied-AGI/3D-Mem)]
* [2024] Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation [[paper](https://arxiv.org/pdf/2410.11989)] [[code](https://github.com/BJHYZJ/DovSG)]
* [2024] Embodied-RAG: General Non-parametric Embodied Memory for Retrieval and Generation [[paper](https://arxiv.org/pdf/2409.18313)]
* [2024] KARMA: Augmenting Embodied AI Agents with Long-and-short Term Memory Systems [[paper](https://arxiv.org/pdf/2409.14908)] [[code](https://github.com/WZX0Swarm0Robotics/KARMA/tree/master)]
* [2024] ReMEmbR: Building and Reasoning Over Long-Horizon Spatio-Temporal Memory for Robot Navigation [[paper](https://arxiv.org/pdf/2409.13682)] [[code](https://github.com/NVIDIA-AI-IOT/remembr)]
* [2024] Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation [[paper](https://arxiv.org/pdf/2403.17846)] [[project](https://hovsg.github.io/)] [[code](https://github.com/hovsg/HOV-SG)]
* [2024] ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning [[paper](https://arxiv.org/pdf/2309.16650)] [[project](https://concept-graphs.github.io/)] [[code](https://github.com/concept-graphs/concept-graphs)]
* [2023] ConceptFusion: Open-set Multimodal 3D Mapping [[paper](https://arxiv.org/pdf/2302.07241)] [[project](https://concept-fusion.github.io/)]

## Reasoning & Planning

* [2026] Bridging Values and Behavior: A Hierarchical Framework for Proactive Embodied Agents [[paper](https://arxiv.org/pdf/2604.27699)]
* [2026] Harnessing Embodied Agents: Runtime Governance for Policy-Constrained Execution [[paper](https://arxiv.org/pdf/2604.07833)]
* [2026] Thinking with Spatial Code for Physical-World Video Reasoning [[paper](https://arxiv.org/pdf/2603.05591)] [[code](https://github.com/Beckschen/spatialcode)]
* [2026] Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs [[paper](https://arxiv.org/pdf/2602.21198)]
* [2026] Agentic AI for Robot Control: Flexible but still Fragile [[paper](https://arxiv.org/pdf/2602.13081)]
* [2026] From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents [[paper](https://arxiv.org/pdf/2602.04326)]
* [2026] Embodied Task Planning via Graph-Informed Action Generation with Large Language Model [[paper](https://arxiv.org/pdf/2601.21841)]
* [2025] Scene Graph-Guided Proactive Replanning for Failure-Resilient Embodied Agent [[paper](https://arxiv.org/pdf/2508.11286)]
* [2025] Conditional Multi-Stage Failure Recovery for Embodied Agents [[paper](https://arxiv.org/pdf/2507.06016)]
* [2025] LERa: Replanning with Visual Feedback in Instruction Following [[paper](https://arxiv.org/pdf/2507.05135)] [[project](https://lera-robo.github.io/)]
* [2025] EMAC+: Embodied Multimodal Agent for Collaborative Planning with VLM+LLM [[paper](https://arxiv.org/pdf/2505.19905)]
* [2023] GPT-4V(ision) for Robotics: Multimodal Task Planning from Human Demonstration [[paper](https://arxiv.org/pdf/2311.12015)] [[code](https://github.com/microsoft/GPT4Vision-Robot-Manipulation-Prompts)]
* [2023] Embodied Task Planning with Large Language Models [[paper](https://arxiv.org/pdf/2307.01848)]
* [2023] SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning [[paper](https://arxiv.org/pdf/2307.06135)] [[project](https://sayplan.github.io/)]
* [2023] VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models [[paper](https://arxiv.org/pdf/2307.05973)] [[project](https://voxposer.github.io/)]
* [2022] LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models [[paper](https://arxiv.org/pdf/2212.04088)] [[project](https://dki-lab.github.io/LLM-Planner)]
* [2022] ProgPrompt: Generating Situated Robot Task Plans using Large Language Models [[paper](https://arxiv.org/pdf/2209.11302)] [[project](https://progprompt.github.io/)]
* [2022] Code as Policies: Language Model Programs for Embodied Control [[paper](https://arxiv.org/pdf/2209.07753)] [[project](https://code-as-policies.github.io/)]
* [2022] Inner Monologue: Embodied Reasoning through Planning with Language Models [[paper](https://arxiv.org/pdf/2207.05608)] [[project](https://innermonologue.github.io/)]
* [2022] SayCan: Do As I Can, Not As I Say: Grounding Language in Robotic Affordances [[paper](https://arxiv.org/pdf/2204.01691)] [[project](https://say-can.github.io/)]
* [2022] Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents [[paper](https://arxiv.org/pdf/2201.07207)] [[project](https://huangwl18.github.io/language-planner)]

## Active

* [2026] Robot Planning and Situation Handling with Active Perception [[paper](https://arxiv.org/pdf/2604.26988)]
* [2026] Explore Like Humans: Autonomous Exploration with Online SG-Memo Construction for Embodied Agents [[paper](https://arxiv.org/pdf/2604.19034)]
* [2026] SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics [[paper](https://arxiv.org/pdf/2603.12193)] [[project](https://lmzpai.github.io/SaPaVe)]
* [2026] See, Act, Adapt: Active Perception for Unsupervised Cross-Domain Visual Adaptation via Personalized VLM-Guided Agent [[paper](https://arxiv.org/pdf/2602.23806)]
* [2026] 3DGSNav: Enhancing Vision-Language Model Reasoning for Object Navigation via Active 3D Gaussian Splatting [[paper](https://arxiv.org/pdf/2602.12159)] [[project](https://aczheng-cai.github.io/3dgsnav.github.io/)]
* [2026] Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration? [[paper](https://arxiv.org/pdf/2602.07055)] [[code](https://github.com/mll-lab-nu/Theory-of-Space)]
* [2025] ActiveVLN: Towards Active Exploration via Multi-Turn RL in Vision-and-Language Navigation [[paper](https://arxiv.org/pdf/2509.12618)]
* [2025] Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation [[paper](https://arxiv.org/pdf/2507.04047)]
* [2025] Enter the Mind Palace: Reasoning and Planning for Long-term Active Embodied Question Answering [[paper](https://arxiv.org/pdf/2507.12846)] [[proceedings](https://proceedings.mlr.press/v305/ginting25a.html)]
* [2025] Uncertainty-Informed Active Perception for Open Vocabulary Object Goal Navigation [[paper](https://arxiv.org/pdf/2506.13367)]
* [2025] WoMAP: World Models For Embodied Open-Vocabulary Object Localization [[paper](https://arxiv.org/pdf/2506.01600)] [[project](https://robot-womap.github.io/)]
* [2024] AP-VLM: Active Perception Enabled by Vision-Language Models [[paper](https://arxiv.org/pdf/2409.17641)]
* [2024] Discovering Object Attributes by Prompting Large Language Models with Perception-Action APIs [[paper](https://arxiv.org/pdf/2409.15505)] [[project](https://prg.cs.umd.edu/EmbodiedAttributeDetection)]
* [2024] Explore until Confident: Efficient Exploration for Embodied Question Answering [[paper](https://arxiv.org/pdf/2403.15941)] [[project](https://explore-eqa.github.io/)] [[code](https://github.com/Stanford-ILIAD/explore-eqa)]

## Navigation

* [2026] LiveVLN: Breaking the Stop-and-Go Loop in Vision-Language Navigation [[paper](https://arxiv.org/pdf/2604.19536)] [[code](https://github.com/NIneeeeeem/LiveVLN)]
* [2026] AnyImageNav: Any-View Geometry for Precise Last-Meter Image-Goal Navigation [[paper](https://arxiv.org/pdf/2604.05351)]
* [2026] Stop Wandering: Efficient Vision-Language Navigation via Metacognitive Reasoning [[paper](https://arxiv.org/pdf/2604.02318)]
* [2026] ImagiNav: Scalable Embodied Navigation via Generative Visual Prediction and Inverse Dynamics [[paper](https://arxiv.org/pdf/2603.13833)] [[project](https://j1dan.github.io/ImagiNav/)]
* [2026] MerNav: A Highly Generalizable Memory-Execute-Review Framework for Zero-Shot Object Goal Navigation [[paper](https://arxiv.org/pdf/2602.05467)] [[project](https://qidekang.github.io/MerNav.github.io/)]
* [2026] Spatial-VLN: Zero-Shot Vision-and-Language Navigation With Explicit Spatial Perception and Exploration [[paper](https://arxiv.org/pdf/2601.12766)] [[project](https://yueluhhxx.github.io/Spatial-VLN-web/)]
* [2026] SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation [[paper](https://arxiv.org/pdf/2601.06806)] [[project](https://imnearth.github.io/Spatial-X/)]
* [2025] MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation [[paper](https://arxiv.org/pdf/2511.10376)]
* [2025] MUVLA: Learning to Explore Object Navigation via Map Understanding [[paper](https://arxiv.org/pdf/2509.25966)]
* [2025] VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation [[paper](https://arxiv.org/pdf/2509.18592)]
* [2025] StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling [[paper](https://arxiv.org/pdf/2507.05240)] [[project](https://streamvln.github.io/)]
* [2024] Navigation with VLM framework: Go to Any Language [[paper](https://arxiv.org/pdf/2410.02787)]
* [2024] NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models [[paper](https://arxiv.org/pdf/2407.12366)]
* [2024] NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation [[paper](https://arxiv.org/pdf/2402.15852)]
* [2024] MapGPT: Map-Guided Prompting with Adaptive Path Planning for Vision-and-Language Navigation [[paper](https://arxiv.org/pdf/2401.07314)] [[code](https://github.com/chen-judge/MapGPT)]
* [2023] VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation [[paper](https://arxiv.org/pdf/2312.03275)] [[project](https://naoki.io/portfolio/vlfm)]
* [2023] GOAT: GO to Any Thing [[paper](https://arxiv.org/pdf/2311.06430)] [[project](https://theophilegervet.github.io/projects/goat/)]
* [2023] NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models [[paper](https://arxiv.org/pdf/2305.16986)]
* [2023] Can an Embodied Agent Find Your "Cat-shaped Mug"? LLM-Guided Exploration for Zero-Shot Object Navigation [[paper](https://arxiv.org/pdf/2303.03480)]
* [2023] ESC: Exploration with Soft Commonsense Constraints for Zero-shot Object Navigation [[paper](https://arxiv.org/pdf/2301.13166)]
* [2022] LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action [[paper](https://arxiv.org/pdf/2207.04429)] [[project](https://sites.google.com/view/lmnav)]

## EQA

* [2026] Memory-Guided View Refinement for Dynamic Human-in-the-loop EQA [[paper](https://arxiv.org/pdf/2603.09541)]
* [2026] FAST-EQA: Efficient Embodied Question Answering with Global and Local Region Relevancy [[paper](https://arxiv.org/pdf/2602.15813)]
* [2025] DarkEQA: Benchmarking Vision-Language Models for Embodied Question Answering in Low-Light Indoor Environments [[paper](https://arxiv.org/pdf/2512.24985)]
* [2025] StreamEQA: Towards Streaming Video Understanding for Embodied Scenarios [[paper](https://arxiv.org/pdf/2512.04451)]
* [2025] BridgeEQA: Virtual Embodied Agents for Real Bridge Inspections [[paper](https://arxiv.org/pdf/2511.12676)] [[project](https://drags99.github.io/bridge-eqa/)]
* [2025] Multi-Step Reasoning for Embodied Question Answering via Tool Augmentation [[paper](https://arxiv.org/pdf/2510.20310)] [[project](https://tooleqa.github.io/)]
* [2025] IndustryEQA: Pushing the Frontiers of Embodied Question Answering in Industrial Scenarios [[paper](https://arxiv.org/pdf/2505.20640)]
* [2025] Memory-Centric Embodied Question Answering [[paper](https://arxiv.org/pdf/2505.13948)]
* [2025] Beyond the Destination: A Novel Benchmark for Exploration-Aware Embodied Question Answering [[paper](https://arxiv.org/pdf/2503.11117)] [[project](https://hcplab-sysu.github.io/EXPRESS-Bench/)]
* [2025] CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space [[paper](https://arxiv.org/pdf/2502.12532)] [[code](https://github.com/BiluYong/CityEQA)]
* [2024] GraphEQA: Using 3D Semantic Scene Graphs for Real-time Embodied Question Answering [[paper](https://arxiv.org/pdf/2412.14480)] [[project](https://saumyasaxena.github.io/grapheqa/)]
* [2024] EfficientEQA: An Efficient Approach for Open Vocabulary Embodied Question Answering [[paper](https://arxiv.org/pdf/2410.20263)] [[code](https://github.com/chengkaiAcademyCity/EfficientEQA)]
* [2024] S-EQA: Tackling Situational Queries in Embodied Question Answering [[paper](https://arxiv.org/pdf/2405.04732)]
* [2024] OpenEQA: Embodied Question Answering in the Era of Foundation Models [[paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.pdf)] [[project](https://open-eqa.github.io/)]

## Manipulation

* [2026] Zero-shot Interactive Perception [[paper](https://arxiv.org/pdf/2602.18374)]
* [2025] FrankenBot: Brain-Morphic Modular Orchestration for Robotic Manipulation with Vision-Language Models [[paper](https://arxiv.org/pdf/2506.21627)]
* [2025] Gondola: Grounded Vision Language Planning for Generalizable Robotic Manipulation [[paper](https://arxiv.org/pdf/2506.11261)] [[project](https://cshizhe.github.io/projects/robot_gondola.html)]
* [2025] From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation [[paper](https://arxiv.org/pdf/2505.08548)] [[project](https://embodied-fsd.github.io/)]
* [2025] Vision-Language Model Predictive Control for Manipulation Planning and Trajectory Generation [[paper](https://arxiv.org/pdf/2504.05225)] [[code](https://github.com/PPjmchen/VLMPC)]
* [2025] Reflective Planning: Vision-Language Models for Multi-Stage Long-Horizon Robotic Manipulation [[paper](https://arxiv.org/pdf/2502.16707)] [[project](https://reflect-vlm.github.io/)]
* [2024] CoPa: General Robotic Manipulation through Spatial Constraints of Parts with Foundation Models [[paper](https://arxiv.org/pdf/2403.08248)] [[project](https://copa-2024.github.io/)]
* [2024] MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting [[paper](https://arxiv.org/pdf/2403.03174)] [[project](https://moka-manipulation.github.io/)]
* [2023] ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation [[paper](https://arxiv.org/pdf/2312.16217)] [[project](https://sites.google.com/view/manipllm)]

## Related Lists

* Awesome Embodied VLA/VA/VLN [[repo](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)]
* Awesome Embodied AI [[repo](https://github.com/wadeKeith/Awesome-Embodied-AI)]
* Awesome Embodied AI [[repo](https://github.com/haoranD/Awesome-Embodied-AI)]
* Awesome Embodied Robotics and Agent [[repo](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent)]
* Awesome Embodied Vision [[repo](https://github.com/ChanganVR/awesome-embodied-vision)]
* Awesome Vision-and-Language Navigation [[repo](https://github.com/eric-ai-lab/awesome-vision-language-navigation)]
* Awesome-Agentic-MLLMs [[repo](https://github.com/HJYao00/Awesome-Agentic-MLLMs)]
* Awesome-Robotics-Foundation-Models [[repo](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models)]
* Awesome 3D Scene Representation for Robotics [[repo](https://github.com/dtc111111/awesome-3dgs-for-robotics)]

<!-- ## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for scope, formatting, and submission guidelines. -->
