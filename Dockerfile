FROM alpine

WORKDIR /home

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


EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
