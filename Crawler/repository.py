# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com

# < Repository >
# This class allows the developer to collect information about a particular repository
# organization = The organization of the repository
# Name = The repository name
# Crawler = A crawler object


class Repository:

    def __init__(self, organization, name, crawler):
        self.name = name
        self.organization = organization
        self.github = crawler

    # Returns general information about the repository
    # https://developer.github.com/v3/repos/#get

    def get(self):
        print '[Repository] Returning general information'
        return self.github.request('repos/' + self.organization + '/' + self.name)

    # Returns the programming languages used in the repository
    # https://developer.github.com/v3/repos/#list-languages

    def languages(self):
        print '[Repository] Returning languages used in the project'
        return self.github.request('repos/' + self.organization + '/' + self.name + '/languages')

    # Returns commit's in the project
    # All parameters are optional. Read more about:
    # https://developer.github.com/v3/repos/commits/#list-commits-on-a-repository

    def commits(self, sha=None, path=None, author=None,
                since=None, until=None, page_range=None):

        commits = []
        parameters = []

        if sha is not None:
            parameters.append('sha=' + sha)

        if path is not None:
            parameters.append('path=' + path)

        if author is not None:
            parameters.append('author=' + author)

        if since is not None:
            parameters.append('since=' + since)

        if until is not None:
            parameters.append('until=' + until)

        if page_range is not None:
            first_page = page_range[0]
            last_page = page_range[1]

            print '[Repository] Returning commits in a page range'
            for page_number in range(first_page, last_page):
                request = self.github.request('repos/' + self.organization + '/' +
                                              self.name + '/commits', parameters + ['page=' + str(page_number)])

                for commit in request:
                    commits.append(commit)

        else:
            print '[Repository] Returning all commits in the project'
            request = ['Waiting for requisition...']
            page_number = 1

            while(request):
                request = self.github.request('repos/' + self.organization + '/' +
                                              self.name + '/commits', parameters + ['page=' + str(page_number)])

                if request:
                    for commit in request:
                        commits.append(commit)

                page_number = page_number + 1

        return commits

    # Returns a specific pull request according to its number
    # https://developer.github.com/v3/pulls/#get-a-single-pull-request

    def pull_request(self, number):
        print '[Repository] Returning pull-request #' + str(number) + ' from project'
        return self.github.request('repos/' + self.organization + '/' + self.name + '/pulls/' + str(number))

    # Returns pull requests in the project
    # All parameters are optional. Read more about:
    # https://developer.github.com/v3/pulls/#list-pull-requests

    def pull_requests(self, state=None, direction=None, sort=None,
                      base=None, head=None, page_range=None):

        pull_requests = []
        parameters = []

        if state is not None:
            parameters.append('state=' + state)

        if direction is not None:
            parameters.append('direction=' + direction)

        if sort is not None:
            parameters.append('sort=' + sort)

        if base is not None:
            parameters.append('base=' + base)

        if head is not None:
            parameters.append('head=' + head)

        if page_range is not None:
            first_page = page_range[0]
            last_page = page_range[1]

            print '[Repository] Returning pull-requests in a page range'
            for page_number in range(first_page, last_page):
                request = self.github.request('repos/' + self.organization + '/' +
                                              self.name + '/pulls', parameters + ['page=' + str(page_number)])

                for pull in request:
                    pull_requests.append(pull)

        else:
            print '[Repository] Returning all pull-requests in the project'
            request = ['Waiting for requisition...']
            page_number = 1

            while(request):
                request = self.github.request('repos/' + self.organization + '/' +
                                              self.name + '/pulls', parameters + ['page=' + str(page_number)])

                if request:
                    for pull in request:
                        pull_requests.append(pull)

                page_number = page_number + 1

        return pull_requests

    # Returns a specific issue according to its number
    # https://developer.github.com/v3/issues/#get-a-single-issue

    def issue(self, number):
        print '[Repository] Returning issue #' + str(number) + ' from project'
        return self.github.request('repos/' + self.organization + '/' + self.name + '/issues/' + str(number))

    # Returns all issues in the project, or in a range
    # All parameters are optional. Read more about:
    # https://developer.github.com/v3/issues/#list-issues-for-a-repository

    def issues(self, state=None, direction=None, milestone=None, labels=None,
               creator=None, since=None, assignee=None, mentioned=None, page_range=None):

        issues = []
        parameters = []

        if state is not None:
            parameters.append('state=' + state)

        if direction is not None:
            parameters.append('direction=' + direction)

        if labels is not None:
            parameters.append('labels=' + labels)

        if creator is not None:
            parameters.append('creator=' + creator)

        if since is not None:
            parameters.append('since=' + since)

        if milestone is not None:
            parameters.append('milestone=' + milestone)

        if mentioned is not None:
            parameters.append('mentioned=' + mentioned)

        if assignee is not None:
            parameters.append('assignee=' + assignee)

        if page_range is not None:
            first_page = page_range[0]
            last_page = page_range[1]

            print '[Repository] Returning issues in a page range'
            for page_number in range(first_page, last_page):
                request = self.github.request('repos/' + self.organization + '/' +
                                              self.name + '/issues', parameters + ['page=' + str(page_number)])

                for issue in request:
                    issues.append(issue)

        else:
            print '[Repository] Returning all issues in the project'
            request = ['Waiting for requisition...']
            page_number = 1

            while(request):
                request = self.github.request('repos/' + self.organization + '/' +
                                              self.name + '/issues', parameters + ['page=' + str(page_number)])

                if request:
                    for issue in request:
                        issues.append(issue)

                page_number = page_number + 1

        return issues

    # Returns all contributors in the project, or in a range
    # All parameters are optional. Read more about:
    # https://developer.github.com/v3/repos/#list-contributors

    def contributors(self, anonymous='false', page_range=None):
        contributors = []

        if page_range is not None:
            first_page = page_range[0]
            last_page = page_range[1]

            print '[Repository] Returning contributors in a page range'

            for page_number in range(first_page, last_page):
                request = self.github.request('repos/' + self.organization + '/' + self.name +
                                              '/contributors', ['page=' + str(page_number), 'anon=' + str(anonymous)])

                for contributor in request:
                    contributors.append(contributor)
        else:
            print '[Repository] Returning all contributors in the project'
            request = ['Waiting for requisition']
            page_number = 1

            while(request):
                request = self.github.request('repos/' + self.organization + '/' + self.name +
                                              '/contributors', ['page=' + str(page_number), 'anon=' + str(anonymous)])

                if request:
                    for contributor in request:
                        contributors.append(contributor)

                page_number = page_number + 1

        return contributors


    def stars(self, page_range=None):
        stars = []
        parameters = []

        if page_range is not None:
            first_page = page_range[0]
            last_page = page_range[1]

            print '[Repository] Returning stars in a page range'

            for page_number in range(first_page, last_page):
                request = self.github.request('repos/' + self.organization + '/' + self.name +
                                              '/stargazers', parameters + ['page=' + str(page_number)])

                for star in request:
                    stars.append(star)
        else:
            print '[Repository] Returning all stars in the project'
            request = ['Waiting for requisition']
            page_number = 1

            while(request):
                request = self.github.request('repos/' + self.organization + '/' + self.name +
                                              '/stargazers', parameters + ['page=' + str(page_number)])

                if request:
                    for star in request:
                        stars.append(star)

                page_number = page_number + 1

        return stars

    def forks(self, sort=None, page_range=None):
        forks = []
        parameters = []

        if sort is not None:
            parameters.append(sort)

        if page_range is not None:
            first_page = page_range[0]
            last_page = page_range[1]

            print '[Repository] Returning forks in a page range'

            for page_number in range(first_page, last_page):
                request = self.github.request('repos/' + self.organization + '/' + self.name +
                                              '/forks', parameters + ['page=' + str(page_number)])

                for fork in request:
                    forks.append(fork)
        else:
            print '[Repository] Returning all forks in the project'
            request = ['Waiting for requisition']
            page_number = 1

            while(request):
                request = self.github.request('repos/' + self.organization + '/' + self.name +
                                              '/forks', parameters + ['page=' + str(page_number)])

                if request:
                    for fork in request:
                        forks.append(fork)

                page_number = page_number + 1

        return forks

    def commits_in_pull_request(self, number):
        commits = []
        request = ['Waiting for requisition']
        page_number = 1

        print '[Repository] Returning all commits in pull request #' + str(number)

        while(request):
            request = self.github.request('repos/' + self.organization + '/' + self.name +
                                          '/pulls/' + str(number) + '/commits', ['page=' + str(page_number)])
            if request:
                for commit in request:
                    commits.append(commit)
            
            page_number = page_number + 1

        return commits

    def comments_in_pull_request(self, number):
        comments = []
        request = ['Waiting for requisition']
        page_number = 1

        print '[Repository] Returning all comments in pull request #' + str(number)

        while(request):
            request = self.github.request('repos/' + self.organization + '/' + self.name +
                                          '/issues/' + str(number) + '/comments', ['page=' + str(page_number)])
            if request:
                for comment in request:
                    comments.append(comment)
            
            page_number = page_number + 1

        return comments

    def reviews_in_pull_request(self, number):
        reviews = []
        request = ['Waiting for requisition']
        page_number = 1

        print '[Repository] Returning all reviews in pull request #' + str(number)

        while(request):
            request = self.github.request('repos/' + self.organization + '/' + self.name +
                                          '/pulls/' + str(number) + '/comments', ['page=' + str(page_number)])
            if request:
                for review in request:
                    reviews.append(review)
            
            page_number = page_number + 1

        return reviews

    def commit_information(self, url):
        url = url.replace('https://api.github.com/', '')
        information = self.github.request(url)
        return information
        
    def files_in_pull_request(self, number):
        files = []
        request = ['Waiting for requisition']
        page_number = 1

        print '[Repository] Returning all files in pull request #' + str(number)

        while(request):
            request = self.github.request('repos/' + self.organization + '/' + self.name +
                                          '/pulls/' + str(number) + '/files', ['page=' + str(page_number)])
            if request:
                for file in request:
                    files.append(file)
            
            page_number = page_number + 1

        return files

    def contributor(self, name):
        return self.github.request('users/' + name)