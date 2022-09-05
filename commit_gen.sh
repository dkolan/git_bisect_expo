#!/bin/bash

function create_commit {
  MESSAGE="This is a line addition $1"
  echo "#$MESSAGE" >> shapes.py
  git add shapes.py
  git commit -m "$MESSAGE"
}

BUGINDEX=$((RANDOM%500))

git branch -D bug_branch
git checkout -b bug_branch

for i in $(seq 1 $BUGINDEX); do
  create_commit $i
done

git cherry-pick origin/has_a_bug

for i in $(seq $((BUGINDEX+1)) 500); do
  create_commit $i
done