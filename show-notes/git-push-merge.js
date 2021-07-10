/* How to Push and Merge a Remote Branch in Git


Github will try to be as efficient as possible and assume you
would want to keep the remote branch only on your local machine
and so will not display the remote branch online.

To actively push the new remote branch:

git push -u origin another-feature

//Enumerating objects: 11, done.
//Counting objects: 100% (11/11), done.
//Delta compression using up to 8 threads
//Compressing objects: 100% (8/8), done.
//Writing objects: 100% (8/8), 1.35 KiB | 692.00 KiB/s, done.
//Total 8 (delta 1), reused 0 (delta 0), pack-reused 0
//remote: Resolving deltas: 100% (1/1), completed with 1 local
//object.
//remote: 
//remote: Create a pull request for 'another-feature' on GitHub
//by visiting:
//remote:      https://github.com/drakotech/git/pull/new/another-feature
//remote:
//To https://github.com/drakotech/git.git
// * [new branch]      another-feature -> another-feature
//Branch 'another-feature' set up to track remote branch 
//'another-feature' from 'origin'.

*/