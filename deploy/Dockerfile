ARG BASE
FROM $BASE

ARG VCS_REF
ARG BUILD_DATE
ENV GIT_COMMIT $VCS_REF

# Metadata
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name="proj-image" \
      org.label-schema.build-date=$BUILD_DATE

WORKDIR /app
COPY . .

ENV DJANGO_SETTINGS_MODULE proj.settings.build
RUN python manage.py makemessages
RUN python manage.py compilemessages
RUN python manage.py collectstatic --noinput --clear

ENTRYPOINT ["./entrypoint.sh"]
