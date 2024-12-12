from ensure import ensure

ensure(1).is_an(int)
ensure({1: {2: 3}}).equals({1: {2: 3}}).also.contains(1)
ensure({1: "a"}).has_key(1).whose_value.has_length(1)
ensure.each_of([{1: 2}, {3: 4}]).is_a(dict).of(int).to(int)
ensure(int).called_with("1100101", base=2).returns(101)
ensure(dict).called_with(1, 2).raises(TypeError)
check(1).is_a(float).or_raise(Exception, "An error happened: {msg}. See http://example.com for more information.")