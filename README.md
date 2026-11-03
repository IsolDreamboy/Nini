# Nini
Criação de um sistema multiagente focado na diminuição de erros médicos, visando principalmente a otimização de sistemas hospitalares para melhor utilização de sua infraestrutura.

(dados docker) docker exec -it nini_db psql -U isol -d triagem_db -c "SELECT id, nome_completo, classificacao_risco, criado_em FROM prontuarios_triagem;"
(server api) uv run uvicorn app.main:app --reload --port 8019   
docker compose up (ou down) -d (ou -v se for down.)
docker volume prune -f
