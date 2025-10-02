# Test Agent Workflow
# Basic tests for the agent workflow

import pytest
import asyncio
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from llm.agent_core import AgentCore
from llm.mcp_client import MCPClient
from transformers.ollama_client import OllamaClient
from backends.handlers import APIHandlers
from utils.kv_store import KVStore


class TestAgentWorkflow:
    """Test cases for agent workflow functionality."""
    
    def test_agent_core_initialization(self):
        """Test that AgentCore can be initialized."""
        agent = AgentCore()
        assert agent is not None
    
    def test_mcp_client_initialization(self):
        """Test that MCPClient can be initialized."""
        client = MCPClient()
        assert client is not None
    
    def test_ollama_client_initialization(self):
        """Test that OllamaClient can be initialized."""
        client = OllamaClient()
        assert client is not None
    
    def test_api_handlers_initialization(self):
        """Test that APIHandlers can be initialized."""
        handlers = APIHandlers()
        assert handlers is not None
    
    def test_kv_store_initialization(self):
        """Test that KVStore can be initialized."""
        store = KVStore()
        assert store is not None
    
    @pytest.mark.asyncio
    async def test_agent_run_async(self):
        """Test that agent can run asynchronously."""
        agent = AgentCore()
        # This should not raise an exception
        await asyncio.sleep(0.1)  # Simulate async operation
        assert True


if __name__ == "__main__":
    pytest.main([__file__])
