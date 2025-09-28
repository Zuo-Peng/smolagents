#!/usr/bin/env python3
"""Setup script for smolagents."""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Define optional dependencies
extras_require = {
    "bedrock": [
        "boto3>=1.36.18"
    ],
    "torch": [
        "torch",
        "torchvision",
        "numpy>=1.21.2",
    ],
    "audio": [
        "soundfile",
        "smolagents[torch]",
    ],
    "docker": [
        "docker>=7.1.0",
        "websocket-client",
    ],
    "e2b": [
        "e2b-code-interpreter>=1.0.3",
        "python-dotenv>=1.0.1",
    ],
    "gradio": [
        "gradio>=5.14.0",
    ],
    "litellm": [
        "litellm>=1.60.2",
    ],
    "mcp": [
        "mcpadapt>=0.1.13",
        "mcp",
    ],
    "mlx-lm": [
        "mlx-lm",
    ],
    "modal": [
        "modal>=1.1.3",
        "websocket-client",
    ],
    "openai": [
        "openai>=1.58.1"
    ],
    "telemetry": [
        "arize-phoenix",
        "opentelemetry-sdk",
        "opentelemetry-exporter-otlp",
        "openinference-instrumentation-smolagents>=0.1.15"
    ],
    "toolkit": [
        "ddgs>=9.0.0",
        "markdownify>=0.14.1",
    ],
    "transformers": [
        "accelerate",
        "transformers>=4.0.0",
        "smolagents[torch]",
    ],
    "vision": [
        "helium",
        "selenium",
    ],
    "vllm": [
        "vllm",
        "torch"
    ],
    "quality": [
        "ruff>=0.9.0",
    ],
    "test": [
        "ipython>=8.31.0",
        "pandas>=2.2.3",
        "pytest>=8.1.0",
        "pytest-datadir",
        "pytest-timeout",
        "python-dotenv>=1.0.1",
        "smolagents[all]",
        "rank-bm25",
        "Wikipedia-API>=0.8.1",
        "mlx[cpu]",
    ],
    "dev": [
        "smolagents[quality,test]",
        "sqlalchemy",
    ],
}

# Add 'all' extra that includes most optional dependencies
extras_require["all"] = [
    "smolagents[audio,docker,e2b,gradio,litellm,mcp,mlx-lm,modal,openai,telemetry,toolkit,transformers,vision,bedrock]",
]

setup(
    name="smolagents",
    version="1.23.0.dev0",
    description="> smolagents: a barebones library for agents. Agents write python code to call tools or orchestrate other agents.",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Aymeric Roucher",
    author_email="aymeric@hf.co",
    url="https://github.com/huggingface/smolagents",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "huggingface-hub>=0.31.2",
        "requests>=2.32.3",
        "rich>=13.9.4",
        "jinja2>=3.1.4",
        "pillow>=10.0.1",  # Security fix for CVE-2023-4863
        "python-dotenv"
    ],
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "smolagent=smolagents.cli:main",
            "webagent=smolagents.vision_web_browser:main",
        ],
    },
    package_data={
        "smolagents.prompts": ["*.yaml"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="agents, ai, artificial intelligence, machine learning, transformers, huggingface",
    license="Apache 2.0",
)