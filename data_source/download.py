import os
import ssl
import urllib.request

import certifi
import wget

pdf_links = [
    {
        "title": "A Comprehensive Overview of Large Language Models",
        "url": "https://arxiv.org/pdf/2307.06435",
    },
    {
        "title": "A Survey of Large Language Models",
        "url": "https://arxiv.org/pdf/2303.18223",
    },
    {
        "title": "The Impact of Large Language Models on Scientific Discovery: a Preliminary Study using GPT-4",
        "url": "https://arxiv.org/pdf/2311.07361",
    },
    {
        "title": "Tracing the Influence of Large Language Models across the Most Impactful Scientific Works",
        "url": "https://www.mdpi.com/2079-9292/12/24/4957/pdf",
    },
    {
        "title": "Topics, Authors, and Institutions in Large Language Model Research: Trends from 17K arXiv Papers",
        "url": "https://arxiv.org/pdf/2307.10700",
    },
    {
        "title": "MemoryBank: Enhancing Large Language Models with Long-Term Memory",
        "url": "https://arxiv.org/pdf/2311.10194",
    },
    {
        "title": "Causal Reasoning and Large Language Models: Opening a New Frontier",
        "url": "https://arxiv.org/pdf/2305.00050",
    },
    {
        "title": "Automatically Correcting Large Language Models: Surveying the State of the Art",
        "url": "https://arxiv.org/pdf/2308.03188",
    },
    {
        "title": "Eight Things to Know about Large Language Models",
        "url": "https://arxiv.org/pdf/2304.00612",
    },
    {
        "title": "Personalized Autonomous Driving with Large Language Models",
        "url": "https://arxiv.org/pdf/2312.09397",
    },
    {
        "title": "AVIS: Autonomous Visual Information Seeking with Large Language Model Agent",
        "url": "https://arxiv.org/pdf/2310.14414",
    },
    {
        "title": "Vision Language Models in Autonomous Driving and Intelligent Transportation Systems",
        "url": "https://arxiv.org/pdf/2310.14414",
    },
    {
        "title": "Llama 2: Open Foundation and Fine-Tuned Chat Models",
        "url": "https://arxiv.org/pdf/2307.09288",
    },
    {
        "title": "Instruction Tuning for Large Language Models: A Survey",
        "url": "https://arxiv.org/pdf/2308.10792",
    },
    {
        "title": "SparseGPT: Massive Language Models Can Be Accurately Pruned with Minimal Accuracy Loss",
        "url": "https://arxiv.org/pdf/2301.00774",
    },
    {
        "title": "Large Language Models: A Survey",
        "url": "https://arxiv.org/pdf/2402.06196",
    },
    {
        "title": "From Query Tools to Causal Architects: Harnessing Large Language Models",
        "url": "https://arxiv.org/pdf/2311.10194",
    },
    {
        "title": "The Landscape of Large Language Models",
        "url": "https://arxiv.org/pdf/2311.10194",
    },
    {
        "title": "The Recent Large Language Models in NLP",
        "url": "https://ieeexplore.ieee.org/document/10000123",
    },
    {
        "title": "A New Frontier for Causal Reasoning with Large Language Models",
        "url": "https://arxiv.org/pdf/2312.09397",
    },
    {"title": "Attention Is All You Need", "url": "https://arxiv.org/pdf/1706.03762"},
    {
        "title": "BERT- Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "url": "https://arxiv.org/pdf/1810.04805",
    },
    {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "url": "https://arxiv.org/pdf/2201.11903",
    },
    {
        "title": "Denoising Diffusion Probabilistic Models",
        "url": "https://arxiv.org/pdf/2006.11239",
    },
]


def is_exist(pdf_file):
    return os.path.exists(f"./pdf_file/{pdf_file['title'].replace(' ', '_')}.pdf")


# Ensure the directory exists
os.makedirs("./pdf_file", exist_ok=True)

# Create an SSL context to ignore SSL certificate errors
ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Install a global opener that uses this SSL context
https_handler = urllib.request.HTTPSHandler(context=ssl_context)
opener = urllib.request.build_opener(https_handler)
urllib.request.install_opener(opener)

for pdf_file in pdf_links:
    if not is_exist(pdf_file):
        try:
            wget.download(
                pdf_file["url"], f"./pdf_file/{pdf_file['title'].replace(' ', '_')}.pdf"
            )
            print(f"Downloaded: {pdf_file['title']}")
        except Exception as e:
            print(f"Failed to download {pdf_file['title']}: {e}")
    else:
        print(f"{pdf_file['title']} is already downloaded")
