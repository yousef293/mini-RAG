# mini-RAG

### File structure for example
'''bash
MINI-RAG
│
├── app/
│   │
│   ├── main.py                # FastAPI entry point
│   ├── config.py              # environment variables & settings
│   │
│   ├── api/                   # FastAPI routes
│   │   ├── routes_chat.py
│   │   ├── routes_upload.py
│   │   └── routes_search.py
│   │
│   ├── agents/                # LangChain / LangGraph logic
│   │   ├── agent.py
│   │   ├── prompts.py
│   │   └── memory.py
│   │
│   ├── mcp_server/            # ALL MCP logic
│   │   ├── server.py
│   │   ├── tools/
│   │   │   ├── summarize.py
│   │   │   ├── read_file.py
│   │   │   ├── web_search.py
│   │   │   ├── vector_search.py
│   │   │   └── ingest_docs.py
│   │
│   ├── services/              # external integrations
│   │   ├── llm_provider.py
│   │   ├── embeddings.py
│   │   └── web_search_client.py
│   │
│   ├── vector_db/
│   │   ├── qdrant_client.py
│   │   └── schema.py
│   │
│   ├── loaders/               # file readers for different formats
│   │   ├── pdf_loader.py
│   │   ├── docx_loader.py
│   │   ├── txt_loader.py
│   │   └── csv_loader.py
│   │
│   └── utils/
│       ├── chunking.py
│       └── logging.py
│
├── data/
│   ├── uploads/
│   └── vector_store/
│
├── tests/
│   ├── test_agent.py
│   └── test_tools.py
│
├── requirements.txt
├── .env
└── README.md
'''
