gitopen
=====
Whitin your git repository folder type the command line 'gitopen' to pen you git remote url in your  browser.


Usage
=====

::

		$ gitopen
		#this will open in your browser
		#the default remote name is origin

		$ gitopen --repo [remote name]
		# The default name is origin

		$ gitopen --repo awesome
			The remote url named 'awesome' doesn't exist
			try:
				gitopen --repo origin
				gitopen --repo heroku
				gitopen --repo gitbucket
		#in case of error it will output all your git remote name


Todo
=====
task.todo