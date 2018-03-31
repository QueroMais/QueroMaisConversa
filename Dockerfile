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

RUN gem install jekyll

