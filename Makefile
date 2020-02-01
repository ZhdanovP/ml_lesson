run:
	docker run -it --rm -p 443:443 -p 8888:8888 -p 4040:4040 -v $(PWD)/src:/home/jovyan/workspace jupyter/all-spark-notebook