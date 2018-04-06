#!/bin/bash

set -e

gitbook install && gitbook build

echo "Removing old docs..."
rm -rf docs

echo "Recreating docs folder..."
cp -r _book docs

echo "Committing changes..."
git add docs
git commit -m "Automated push"

git push origin master

exit 0
