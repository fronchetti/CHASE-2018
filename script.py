try:
    import Crawler.crawler as GitCrawler
    import Crawler.repository as GitRepository
    import langid.langid
    import multiprocessing
    from datetime import datetime
    from functools import partial
    from collections import OrderedDict
    import re
    import json
    import csv
    import os
except ImportError as error:
    raise ImportError(error)

class Repository():
    def __init__(self, collector, folder):
        self.collector = collector
        self.folder = folder

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def summary_of_contributors(self):
        contributors_file = self.folder + '/contributors.json'

        if os.path.isfile(contributors_file):
            contributors = json.load(open(contributors_file, 'r'))
            with open(self.folder + '/contributors.csv', 'w') as output:
                fieldnames = ['id', 'login', 'employee-or-volunteer', 'url', 'company', 'location', 'blog', 'email', 'biography']
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                writer.writeheader()
                for contributor in contributors:
                    if 'login' in contributor:
                        try:
                            data = self.collector.contributor(contributor['login'])

                            if data['company']:
                                data['company'] = data['company'].encode('utf-8')
                            if data['location']:
                                data['location'] = data['location'].encode('utf-8')
                            if data['blog']:
                                data['blog'] = data['blog'].encode('utf-8')
                            if data['email']:
                                data['email'] = data['email'].encode('utf-8')
                            if data['bio']:
                                data['bio'] = data['bio'].encode('utf-8')

                            if data['site_admin'] == True:
                                writer.writerow({'id': data['id'], 'login': data['login'], 'employee-or-volunteer': 'employee', 'url': data['url'], 'company': data['company'], 'location': data['location'], 'blog': data['blog'], 'email': data['email'], 'biography': data['bio']})
                            else:
                                writer.writerow({'id': data['id'], 'login': data['login'], 'employee-or-volunteer': 'volunteer', 'url': data['url'], 'company': data['company'], 'location': data['location'], 'blog': data['blog'], 'email': data['email'], 'biography': data['bio']})
                        except:
                            continue
                    else:
                        print contributor
    # General information about the repository (Source: API)
    def about(self):
        about_file = self.folder + '/about.json'

        if not os.path.isfile(about_file):
            about = self.collector.get()

            with open(about_file, 'w') as file:
                json.dump(about, file, indent = 4)

    # Pull requests of the repository (Source: API)
    def pull_requests(self):
        pulls_file = self.folder + '/pull_requests.json'

        if not os.path.isfile(pulls_file):
            pull_requests = self.collector.pull_requests(state='all')
    
            with open(pulls_file, 'w') as file:
                json.dump(pull_requests, file, indent = 4)

    # Contributors of the repository (Source: API)
    def contributors(self):
        contributors_file = self.folder + '/contributors.json'

        if not os.path.isfile(contributors_file):
            contributors = self.collector.contributors(anonymous='true')

            for contributor in contributors:
                if 'site_admin' in contributor.keys():
                    # We moved this developers to the internals because we found qualitative evidences that they worked at GitHub
                    if 'atom' in self.folder:
                        if contributor['login'] == 'benogle' or contributor['login'] == 'thedaniel' or contributor['login'] == 'jlord':
                            print contributor['login']
                            contributor['site_admin'] = True
                    if 'hubot' in self.folder:
                        if contributor['login'] == 'bhuga' or contributor['login'] == 'aroben':
                            contributor['site_admin'] = True
                    if 'linguist' in self.folder:
                        if contributor['login'] == 'arfon' or contributor['login'] == 'aroben' or contributor['login'] == 'tnm' or contributor['login'] == 'brandonblack' or contributor['login'] == 'rick':
                            contributor['site_admin'] = True            
                    if 'electron' in self.folder:
                        if contributor['login'] == 'miniak' or contributor['login'] == 'codebytere':
                            contributor['site_admin'] = True

            with open(contributors_file, 'w') as file:
                json.dump(contributors, file, indent = 4)

    # Summary with informations of closed pull requests. (Source: API and pull_requests.json)
    def closed_pull_requests_summary(self):
        pulls_file = self.folder + '/pull_requests.json'
        pulls_summary_file = self.folder + '/pulls_closed.csv'

        if os.path.isfile(pulls_file) and not os.path.isfile(pulls_summary_file):
            with open(pulls_file, 'r') as pulls:
                data = json.load(pulls)

                with open(pulls_summary_file, 'a') as output:
                    fieldnames = ['pull_request', 'number_of_commits', 'number_of_comments','number_of_reviews','user_type', 'user_login', 'closed_at', 'number_of_additions', 'number_of_deletions','number_of_files_changed','number_of_days', 'message', 'number_of_characters', 'second_line_is_blank', 'language']
                    writer = csv.DictWriter(output, fieldnames=fieldnames)
                    writer.writeheader()

                    for pull_request in data:
                        if pull_request['state'] == 'closed' and pull_request['merged_at'] == None:
                            try:
                                number_of_commits = self.collector.commits_in_pull_request(pull_request['number'])
                                number_of_comments = self.collector.comments_in_pull_request(pull_request['number'])
                                number_of_reviews = self.collector.reviews_in_pull_request(pull_request['number'])
                                pull_request_data = self.collector.pull_request(pull_request['number'])

                                number_of_files_changed = None
                                number_of_additions = None
                                number_of_deletions = None
                                message = ''

                                if pull_request_data:
                                    if 'changed_files' in pull_request_data:
                                        number_of_files_changed = pull_request_data['changed_files']
                                    if 'additions' in pull_request_data:
                                        number_of_additions = pull_request_data['additions']
                                    if 'deletions' in pull_request_data:
                                        number_of_deletions = pull_request_data['deletions']
                                    if 'body' in pull_request_data:
                                        if pull_request_data['body'] != None:
                                            message = pull_request_data['body'].encode('utf-8')

                                    number_of_characters = len(message)
                                    second_line_is_blank = False
                                    lines = message.split('\n')

                                    if len(lines) > 1:
                                        if not lines[1].strip():
                                            second_line_is_blank = True

                                    language = langid.classify(message)[0]

                                created_at = datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                                closed_at = datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                                number_of_days = (closed_at - created_at).days

                                if pull_request['user']['site_admin'] == True:
                                    writer.writerow({'number_of_characters': number_of_characters, 'second_line_is_blank': second_line_is_blank, 'language': language, 'pull_request': pull_request['number'], 'number_of_commits': len(number_of_commits), 'number_of_comments': len(number_of_comments), 'number_of_reviews': len(number_of_reviews), 'user_type': 'Internals', 'user_login': pull_request['user']['login'], 'closed_at': closed_at, 'number_of_additions': number_of_additions, 'number_of_deletions': number_of_deletions, 'number_of_files_changed': number_of_files_changed, 'number_of_days': number_of_days, 'message': message})
                                else:
                                    writer.writerow({'number_of_characters': number_of_characters, 'second_line_is_blank': second_line_is_blank, 'language': language, 'pull_request': pull_request['number'], 'number_of_commits': len(number_of_commits), 'number_of_comments': len(number_of_comments), 'number_of_reviews': len(number_of_reviews), 'user_type': 'Externals', 'user_login': pull_request['user']['login'], 'closed_at': closed_at, 'number_of_additions': number_of_additions, 'number_of_deletions': number_of_deletions, 'number_of_files_changed': number_of_files_changed, 'number_of_days': number_of_days, 'message': message})
                            except Exception as ex:
                                with open('error.log', 'a') as errors:
                                    errors.write(ex)
                                    errors.write('\n Repository:' + self.folder + '\n')

    def pull_requests_files(self):
        pulls_file = self.folder + '/pull_requests.json'
        pulls_files_file = self.folder + '/pull_requests_files.json'
        dictionary = {}

        if os.path.isfile(pulls_file):
            with open(pulls_file, 'r') as pulls:
                data = json.load(pulls)

                for pull_request in data:
                    try:
                        if pull_request['state'] == 'closed':
                            files = self.collector.files_in_pull_request(pull_request['number'])
                            dictionary[pull_request['number']] = files
                    except Exception as ex:
                        with open('error.log', 'a') as errors:
                            errors.write(ex)
                            errors.write('\n Repository:' + self.folder + '\n')
         
        with open(pulls_files_file, 'w') as outfile:
            json.dump(dictionary, outfile)

    def contributors_ranking(self):
        pull_requests = json.load(open(self.folder + '/pull_requests.json'))
        internals = {}
        externals = {}

        for pull_request in pull_requests:
            author = pull_request['user']['login']
            if pull_request['user']['site_admin'] == True:
                if author in internals:
                    internals[author] = internals[author] + 1
                else:
                    internals[author] = 1
            else:
                if author in externals:
                    externals[author] = externals[author] + 1
                else:
                    externals[author] = 1

        fieldnames = ['login','url','number_of_contributions']
        writer = csv.DictWriter(open(self.folder + '/internals.csv', 'w'), fieldnames=fieldnames)
        writer.writeheader()

        for key in sorted(internals, key=internals.get, reverse=True):
            writer.writerow({'login': key, 'url': 'https://github.com/' + key, 'number_of_contributions': internals[key]})

        writer = csv.DictWriter(open(self.folder + '/externals.csv', 'w'), fieldnames=fieldnames)
        writer.writeheader()

        for key in sorted(externals, key=externals.get, reverse=True):
            writer.writerow({'login': key, 'url': 'https://github.com/' + key, 'number_of_contributions': externals[key]})

    def pull_requests_files_analysis(self):
        pulls_summary_file = self.folder + '/pulls_merged.csv' # Change it to merge if you want ;-)
        pulls_summary_file_updated = self.folder + '/pulls_merged_updated' # Change it to merge if you want ;-)
        pulls_files_file = self.folder + '/pull_requests_files.json'
        regex = re.compile(r'.*test.*\.[^.]+$')

        if os.path.isfile(pulls_summary_file) and os.path.isfile(pulls_files_file):
            input_file = open(pulls_summary_file, 'r')
            reader = csv.DictReader(input_file)
            output_file = open(pulls_summary_file_updated, 'w')
            writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames + ['number_of_test_files'])
            writer.writeheader()
            output_file = open(self.folder + '/unit_test_files.csv', 'w')
            writer = csv.DictWriter(output_file, fieldnames=['pull_request', 'unit_test_files'])
            writer.writeheader()
            json_file = json.load(open(pulls_files_file, 'r'))

            for pull_request in reader:
                unit_test_files = []
                number_of_test_files = 0

                for pull_request_number in json_file:
                    if int(pull_request['pull_request']) == int(pull_request_number):
                        files = json_file[pull_request_number]
                        
                        for file in files:
                            filename = file['filename'].split('/')[-1]
                            if regex.search(filename):
                                unit_test_files.append(filename)
                                number_of_test_files = number_of_test_files + 1
                        
                        if len(unit_test_files) > 0:
                            if 'atom' in self.folder:
                                writer.writerow({'pull_request': 'https://github.com/atom/atom/pull/' + str(pull_request_number) + '/files', 'unit_test_files': ','.join(unit_test_files)})
                            if 'electron' in self.folder:
                                writer.writerow({'pull_request': 'https://github.com/electron/electron/pull/' + str(pull_request_number) + '/files', 'unit_test_files': ','.join(unit_test_files)})
                            if 'hubot' in self.folder:
                                writer.writerow({'pull_request': 'https://github.com/hubotio/hubot/pull/' + str(pull_request_number) + '/files', 'unit_test_files': ','.join(unit_test_files)})
                            if 'git-lfs' in self.folder:
                                writer.writerow({'pull_request': 'https://github.com/github/git-lfs/pull/' + str(pull_request_number) + '/files', 'unit_test_files': ','.join(unit_test_files)})
                            if 'linguist' in self.folder:
                                writer.writerow({'pull_request': 'https://github.com/github/linguist/pull/' + str(pull_request_number) + '/files', 'unit_test_files': ','.join(unit_test_files)})

                pull_request['number_of_test_files'] = number_of_test_files
                writer.writerow(pull_request)

def repositories_in_parallel(project):
    collector = GitRepository.Repository(project['organization'], project['name'], crawler)
    folder = dataset_folder + project['name']

    R = Repository(collector, folder)
    # R.about()
    # R.contributors()
    # R.pull_requests()
    # R.pull_requests_files()
    #R.pull_requests_files_analysis()
    # R.closed_pull_requests_summary()
    # R.update_summaries()
    # R.update_second_line_is_blank()
    # R.summary_of_contributors()
    R.contributors_ranking()

if __name__ == '__main__':
    dataset_folder = 'Dataset/'
    projects = [{'organization':'electron','name':'electron'},
    {'organization':'github','name':'linguist'},
    {'organization':'git-lfs','name':'git-lfs'},
    {'organization':'hubotio','name':'hubot'},
    {'organization':'atom','name':'atom'}]

    if not os.path.exists(dataset_folder):
        os.makedirs(dataset_folder)

    api_client_id = '4161a8257efaea420c94' # Please, specify your own client id
    api_client_secret = 'd814ec48927a6bd62c55c058cd028a949e5362d4' # Please, specify your own client secret
    crawler = GitCrawler.Crawler(api_client_id, api_client_secret)
    # Multiprocessing technique
    parallel = multiprocessing.Pool(processes=4) # Define number of processes
    parallel.map(partial(repositories_in_parallel), projects)