FROM python:3

COPY backend /apps/backend

COPY temp_data /apps/temp_data

COPY data_harvest /apps/data_harvest

RUN pip install flask_cors \
 && pip install couchdb \
 && pip install numpy \
 && pip install requests
RUN cd /apps/data_harvest/aurinData && python exportToCouchdb.py \
 && cd /apps/data_harvest/TimelineData && python exportJson.py

RUN cd /apps/backend && python dataclean(1).py

RUN pip install flask_cors

WORKDIR /apps/backend

EXPOSE 5000

CMD ["flask","run"]

