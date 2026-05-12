---
type: clip
title: "Permission Control · open-metadata/OpenMetadata · Discussion #17119 · GitHub"
url: "https://github.com/open-metadata/OpenMetadata/discussions/17119"
clipped: 2026-05-10
origin: web-clip
sources: []
tags: [web-clip]
---

# Permission Control · open-metadata/OpenMetadata · Discussion #17119 · GitHub

Source: https://github.com/open-metadata/OpenMetadata/discussions/17119

Skip to content

You signed in with another tab or window. Reload to refresh your session.

You signed out in another tab or window. Reload to refresh your session.

You switched accounts on another tab or window. Reload to refresh your session.

Dismiss alert

open-metadata

/

OpenMetadata

Public

Notifications

You must be signed in to change notification settings

Fork

2.1k

Star

13.9k

Permission Control

#17119

Unanswered

luckyliush

asked this question in

Q&A

Permission Control

#17119

luckyliush

Jul 22, 2024

·

1 comments

·

5 replies

Return to top

Discussion options

Uh oh!

There was an error while loading. Please reload this page.

Quote reply

luckyliush

Jul 22, 2024

-

Is it possible to restrict users to access only specified information, such as a database or a data table?

I used policies to restrict user permissions, but it did not achieve the desired effect. Although users cannot access certain databases, they can still see their existence on the web page.

Beta

Was this translation helpful?

Give feedback.

1

You must be logged in to vote

All reactions

Replies:

1 comment

·

5 replies

Comment options

Uh oh!

There was an error while loading. Please reload this page.

Quote reply

Prajwal214

Jul 23, 2024

Collaborator

-

@luckyliush You can create a policy based on the tags and assign to the users to view data asset

https://docs.open-metadata.org/v1.4.x/how-to-guides/admin-guide/roles-policies/authorization#building-blocks-of-authorization-rules

Beta

Was this translation helpful?

Give feedback.

1

You must be logged in to vote

All reactions

5 replies

Comment options

Uh oh!

There was an error while loading. Please reload this page.

Quote reply

edited

Uh oh!

There was an error while loading. Please reload this page.

luckyliush

Jul 23, 2024

Author

-

Thank you for your reply

I configured the system according to the official website link you provided, but it did not achieve the expected effect.

First of all, I expect that accounts with different permissions should see different numbers of data tables on the tables page of data assets.

For example, can the function now be achieved that the admin account can see all tables of data assets, and accounts with less permissions cannot see all tables, rather than just being unable to access them but still being able to see them on the web page?

Beta

Was this translation helpful?

Give feedback.

All reactions

Comment options

Uh oh!

There was an error while loading. Please reload this page.

Quote reply

Prajwal214

Jul 24, 2024

Collaborator

-

To restrict users based on tags, you can create policies that control visibility and access to tables with specific tags.

Policy for Admin Users:

"name": "AllowAdminView",

"resource": "Table",

"operation": "View",

"effect": "Allow"

Policy for Non-Admin Users:

"name": "DenyNonAdminViewSensitiveTags",

"resource": "Table",

"operation": "View",

"condition": matchAnyTag:"tag.Sensitive"

"effect": "Deny"

Assign Policies:

Assign the AdminViewPolicy to the admin role.

Assign the RestrictedViewPolicy to non-admin roles.

This setup ensures that non-admin users will not be able to see tables tagged with "Sensitive", effectively hiding them from the tables page. Make Sure you are proving correct FQN for the tag in the policy.

Beta

Was this translation helpful?

Give feedback.

All reactions

Comment options

Uh oh!

There was an error while loading. Please reload this page.

Quote reply

luckyliush

Jul 24, 2024

Author

-

Thank you for your reply. I have configured the policy according to your instructions and added the policy to a role. I assigned the role to a non-admin user, but the user can still see all the tables on the table page of the data asset, although he cannot access them. I have added the PII.Sensitive tag to some tables, hoping not to see them. Is there something wrong with my configuration?

Beta

Was this translation helpful?

Give feedback.

All reactions

Comment options

Uh oh!

There was an error while loading. Please reload this page.

Quote reply

Prajwal214

Jul 25, 2024

Collaborator

-

Can you verify the permission call, what all rules are applied to the user.

Beta

Was this translation helpful?

Give feedback.

All reactions

Comment options

Uh oh!

There was an error while loading. Please reload this page.

Quote reply

edited

Uh oh!

There was an error while loading. Please reload this page.

Prajwal214

Jul 26, 2024

Collaborator

-

Currently we don't hide the data asset from the User in Explore Tab, Search based RBAC will be part of OM v1.6 release.

Beta

Was this translation helpful?

Give feedback.

👍

1

All reactions

👍

1

Sign up for free

to join this conversation on GitHub.

Already have an account?

Sign in to comment

Category

🙏

Q&A

Labels

None yet

2 participants

You can’t perform that action at this time.
