from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",          # ignore any extra env vars not defined here
    )

    # ── OpenAI ──────────────────────────────────────────────────────
    openai_api_key: str
    openai_embedding_model: str = "text-embedding-3-small"
    openai_llm_model: str = "gpt-4o-mini"
    openai_embedding_dimensions: int = 1536

    # ── Pinecone ────────────────────────────────────────────────────
    pinecone_api_key: str
    pinecone_index_name: str = "resumes"
    pinecone_jd_index_name: str = "hireflow-jd"

    app_env: str = "development"
    top_k: int = 5
    min_confidence: float = 0.3


settings = Settings()