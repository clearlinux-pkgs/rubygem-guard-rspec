#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-guard-rspec
Version  : 4.7.2
Release  : 13
URL      : https://rubygems.org/downloads/guard-rspec-4.7.2.gem
Source0  : https://rubygems.org/downloads/guard-rspec-4.7.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# Guard::RSpec
[![Gem Version](https://badge.fury.io/rb/guard-rspec.png)](http://badge.fury.io/rb/guard-rspec) [![Build Status](https://secure.travis-ci.org/guard/guard-rspec.png?branch=master)](http://travis-ci.org/guard/guard-rspec) [![Dependency Status](https://gemnasium.com/guard/guard-rspec.png)](https://gemnasium.com/guard/guard-rspec) [![Code Climate](https://codeclimate.com/github/guard/guard-rspec.png)](https://codeclimate.com/github/guard/guard-rspec) [![Coverage Status](https://coveralls.io/repos/guard/guard-rspec/badge.png?branch=master)](https://coveralls.io/r/guard/guard-rspec)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n guard-rspec-4.7.2
gem spec %{SOURCE0} -l --ruby > rubygem-guard-rspec.gemspec

%build
gem build rubygem-guard-rspec.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
guard-rspec-4.7.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/guard-rspec-4.7.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/.hound.yml
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/.rubocop_todo.yml
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/gemfiles/Gemfile.rspec-2.99
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/gemfiles/Gemfile.rspec-3.4
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/gemfiles/common
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/guard-rspec.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/command.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/deprecator.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/dsl.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/inspectors/base_inspector.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/inspectors/factory.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/inspectors/focused_inspector.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/inspectors/keeping_inspector.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/inspectors/simple_inspector.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/notifier.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/results.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/rspec_process.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/templates/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec_defaults.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/lib/guard/rspec_formatter_results_path.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/acceptance/fixtures/succeeding_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/acceptance/formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/command_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/deprecator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/inspectors/base_inspector_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/inspectors/factory_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/inspectors/focused_inspector_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/inspectors/keeping_inspector_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/inspectors/shared_examples.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/inspectors/simple_inspector_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/notifier_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/results_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/rspec_process_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/runner_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec/template_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec_formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/lib/guard/rspec_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-rspec-4.7.2/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/guard-rspec-4.7.2.gemspec
