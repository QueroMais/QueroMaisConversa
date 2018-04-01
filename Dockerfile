FROM alpine

RUN apk add --update \
	python3 \
	build-base\
	ruby \
	ruby-bundler \
	ruby-irb \
	ruby-dev \
	ruby-rdoc \
	bash 

RUN gem install bundler jekyll

COPY Gemfile . 

RUN bundle update 

WORKDIR /home



EXPOSE 4000

CMD ["jekyll", "serve"]

