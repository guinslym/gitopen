import click, os, re, sys, webbrowser
from blessings import Terminal

#color output
t = Terminal()

###############helper
def read_config_file():
    """This will read your git config file """
    fname = os.path.exists(os.getcwd()+"/.git/config")
    if fname:
        with open(os.getcwd()+'/.git/config') as f:
            content = f.readlines()
        return content
    else:
        click.echo(t.red('Error: ')+ 'This is not a git repository')
        sys.exit()

def hash_of_content(content):
    """This will loop into the content of the file 'config'
    in order to return a hash that contains the repo_name and the repo_url

    ex of return: {'origin':'https://github.com/guinslym/myrepo'}
    """
    repo_name=[]
    repo_url=[]
    for line in content:
        if re.findall(r'"(.*?)"', line):
            repo_name.append(re.findall(r'"(.*?)"', line)[0])
        if 'url = ' in line:
            #https://git.heroku.com/darrasbusiness.git
            if 'heroku' in line:
                line = line.split('url = ')[1]
                line = line.split('.git')[0]
                repo_url.append(line)
            else:
                #git@github.com:guinslym/myrepo.git
                index1 = line.index('@')
                repo_value = line[index1+1:]
                #github.com:guinslym/myrepo.git
                repo = repo_value.replace(':','/')
                #github.com/guinslym/myrepo.git
                index2 = repo.rfind('.')
                repo = repo[:index2]
                #github.com/guinslym/myrepo
                repo_url.append('https://'+repo.strip())
                #https://github.com/guinslym/myrepo
    #print(repo_name) => ['origin', 'heroku', 'gitbucket']
    content ={}
    for i in repo_name:
        index = repo_name.index(i)
        content.update({i: repo_url[index]})
    #print(content)
    return content



#####################
@click.command()
@click.option('--repo', default='origin',
        help='Open a selected repo')
def cli(repo):
    """This scripts open in your the given remote name"""
    content = read_config_file()
    if content == False:
        return 0
    content = hash_of_content(content)
    url = content.get(repo, None)
    if url:
        click.echo('{0}'.format(url))
        webbrowser.open_new_tab(url)
    else:
        #Print error message
        click.echo("The remote url named " + t.red("'{0}'").format(repo) + " doesn't exist".format(repo))
        click.echo('try:')
        for i in content.keys():
            click.echo("\tgitopen --repo "+t.green(i))

'''
@click.command()
@click.option('--remote', default='origin',
        help='Open a selected repo, alias of gitopen --repo')
def cli(remote):
    """Alias of git"""
    content = read_config_file()
    if content == False:
        return 0
    content = hash_of_content(content)
    url = content.get(remote, None)
    if url:
        click.echo('{0}'.format(url))
        webbrowser.open_new_tab(url)
    else:
        #Print error message
        click.echo("The remote url named " + t.red("'{0}'").format(remote) + " doesn't exist".format(remote))
        click.echo('try:')
        for i in content.keys():
            click.echo("\tgitopen --remote "+t.green(i)) 
'''
