FROM python:3

COPY backend /apps/backend

COPY temp_data /apps/temp_data

RUN pip install flask_cors

WORKDIR /apps/backend

EXPOSE 4500

# CMD ["flask","run","-p","4500"]

