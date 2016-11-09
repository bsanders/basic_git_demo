%author: Bill Sanders <billysanders@gmail.com>
%title: Intro to Git



-> ## Who's this? <-

Bill Sanders, CSUSM Alum, ACM President 2012-2013

Worked at Teradata for almost 3 years, now working at a startup called StackIQ in Solana Beach.

[StackIQ](www.stackiq.com) has an Open Source product called [Stacki](www.github.com/StackIQ/stacki) (and we have commercial add-ons).

Stacki is a system that allows you to install several Linux distributions on 'bare metal' (as opposed to virtual/cloud) servers, fully customized and ready to use on the first boot.  It's a super cool project, a fun company, and a great feeling working on Open Source.

  
      ____  _             _    _
     / ___|| |_ __ _  ___| | _(_)
     \___ \| __/ _` |/ __| |/ / |
      ___) | || (_| | (__|   <| |
     |____/ \__\__,_|\___|_|\_\_|


^

Incidentally, we're hiring.

---


-> ## Intro to Git for source control <-


            .-ossyyyysso-.         yyyyyy,         oooooo,
         .ssyyyyyyyyyyyyyyss:      yyyyyy,         oooooo,
       .+yyyyyyyyyyyyyyyyyyyy:.    yyyyyy,         oooooo,
      .yyyyyyyys.````.syyyyyyy:.   yyyyyy,         oooooo,
     .yyyyyyy:          +yyyyyy:   yyyyyy,         oooooo,
     oyyyyyy-            ......`   yyyyyy,         oooooo,
     yyyyyys                       yyyyyy,  oooooooooooooooooooo
    :yyyyyy+       yyyyyyyyyyyy,   yyyyyy,  oooooooooooooooooooo
    .yyyyyyo       yyyyyyyyyyyy,   yyyyyy,  oooooooooooooooooooo
     yyyyyyy`      ``````.syyyy,   yyyyyy,         oooooo,``````
     :yyyyyys.          .:yyyyy,   yyyyyy,         oooooo,
      :yyyyyyy:.      .:oyyyyyy,   yyyyyy,         oooooo,
       :yyyyyyyyyyyyyyyyyyyyyyy,   yyyyyy,         oooooo,
        `:syyyyyyyyyyyyyy: yyyy,   yyyyyy,         oooooo,
           `:+ossyyssoo-`  yyyy,   yyyyyy,         oooooo,

---


-> ## Why Version Control? <-

For groups:

* Coordinating when someone can work on the code is frustrating.
* Manually combining zip files is a pain, and prone to losing a chunk of their work.
* Overwriting someone else's work is a real possibility.

^

-> ## This is all wasted time! <-

^

For yourself:

* What if you make a change that you later find out doesn't work?  Ctrl-Z won't always save you.
* Employers use this shit and expect you to know it (to varying degrees).

^

(and don't work for anyone who doesn't use source control -- huge red flag!) 

---


-> ## Why Git? <-

Git has become the de facto VCS for open source, and is basically heading there for business as well.

Why?


^ 

*Flexibility*

Flexible in terms of how teams/organizations can use it, but it also allows a lot of flexibility to individual developers as well.

^ 

Older version control systems required the developer to have a constant network connection, didn't work over the Internet, forbid developers from working on the same file at the same time.  Some even required manual action from the VCS administrator to create a new branch.  In some cases, they were just plain slow.  With Git, all of these problems go away.

---


-> ## What's so great about Git? <-

Git is:
* Open Source -- free to download, use, modify, redistribute.
* Decentralized -- There is no required One True source for a project.
* Serverless -- Git runs totally locally and requires basically no work to setup or maintain.

All of this means that certain workflows that were impossible prior to Git become easy and in fact natural.  Development can be incredibly distributed.

As far as Git is concerned, your local copy of the Linux kernel is just as valid and important as the one on Linus' desktop, or kernel.org.

What is it not?  A good place to store binary files that will change.  Git stores only the differences between files.  Since binary files are encoded, a small change could mean a change to the entire contents of the encoded file.

---


-> ## Git vs GitHub <-
-> (and GitLab, BitBucket, Gogs, etc) <-

Git is the tool.

GitHub (et al) are simply *centralized* web frontends to the tool.

Git is decentralized.  GitHub is very centralized.

---


-> ## Terminology <-
VCS tools introduce a lot of new terminology

* Repository - a full copy of the project and its version history
* fork - a full copy of a repository, at a point in time
* push - sending changes from a local copy of the repository to a remote (perhaps the original) copy
* pull - fetching changes from a remote copy of the repository
* commit - a point-in-time snapshot of the repository

---
 

Git for better or worse adds to this

* Origin - the name on your system for a particular remote repository's URL; changing origin's URL changes where you push/pull from
* master - is the default name for a branch in Git

These are simply default aliases for common elements in a git repo.

You can and will find other 'remotes' besides 'Origin', and you will have many more branches aside from 'master'

^ 

* staging - staging is the act of preparing a commit.  You can add or remove files (or parts of files!) from staging until you are ready to commit.
* HEAD - is a symbolic reference to the current working revision
* SHA - a commit ID.  A SHA is a 40 character ID for a specific commit.
* Tag - a way to give a user friendly label to a commit "v1.2"
* Parent - the commit prior to the one you're on.

GitHub of course, adds even more terms
pull request, issues

---


-> ## References <-

HEAD, Sha, Tag, etc give you useful ways of referring to commits.  You can also use them in a relative way:  HEAD~2 refers to the commit that is 2 commits before HEAD -- HEAD's grandparent.  You can mix and match them, too.

To see the source code difference between what was tagged as 'v1.0' and the previous commit:
`git diff HEAD~1 v1.0`

Or show what changes went into a specific commit:
`git show a5a145`

Or to see an entire specific file at a specific commit:
`git show aeh34f:foobar.cpp`

There's lots of other ways to specify relative commits...

---


-> ## Starting out <-

`git init` creates an empty database with a default branch named 'master'

    $ git init
    Initialized empty Git repository in /foo/.git/

All of git's data is stored under the .git directory in the project folder (aka repo) -- be careful messing with this!  Deleting it will delete your local copy of the history.

`git add $FILENAME` adds a file to the staging area

`git commit` takes all the data in the staging area, and saves it in Git's database in a single logical unit.

---


--> ## Demo? <--


---


Bill Sanders
Email: billysanders@gmail.com
Github: @bsanders


---


#### Here are some aliases I use in my ~/.gitconfig file
~/.gitconfig:

[alias]
branches = branch -a
remotes = remote -v
tags = tag
stashes = stash list
unstage = reset -q HEAD --
discard = checkout --
uncommit = reset --mixed HEAD~
amend = commit --amend
graph = log --decorate --oneline --all --graph
precommit = diff --cached --diff-algorithm=minimal -w

---

### Other git tutorials, tips.

### _great_ tutorial:
http://rypress.com/tutorials/git/index

https://github.com/git-tips/tips
https://gist.github.com/wayspurrchen/940a21127b77ac1a9720
https://www.reddit.com/r/programming/comments/50xkvx/automatically_locate_when_and_where_bugs_were/
http://ohshitgit.com/



