from worker import *
if __name__ == "__main__":
    data_dir = "./demo"
    emb_model_name = "sentence-transformers/all-MiniLM-L6-v2"

    worker = Worker(data_dir, emb_model_name)

    # Generate the OpenAPI YAML file
    worker.create_openapi_yaml()

    # Generate the RAG Python file
    worker.create_rag_py()

    # Print the system description
    description = worker.__description__()
    print("System Description:", description)

    # Optionally delete the cache
    # worker.delete_cache()
