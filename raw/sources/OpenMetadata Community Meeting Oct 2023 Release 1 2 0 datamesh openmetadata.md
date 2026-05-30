---
title: "OpenMetadata Community Meeting Oct 2023: Release 1 2 0 #datamesh #openmetadata"
source: "https://www.youtube.com/watch?v=Nh2xLAwY2-A&t=2461s"
author:
  - "[[OpenMetadata]]"
published: 2023-10-20
created: 2026-05-14
description: "The OpenMetadata Community Meeting was held on Oct 19th, 2023. In this meeting, we discussed and demoed the latest features in the 1.2.0 Release. Watch the video to learn more about these features:-"
tags:
  - "clippings"
topic:
type: "note"
---
![](https://www.youtube.com/watch?v=Nh2xLAwY2-A)

The OpenMetadata Community Meeting was held on Oct 19th, 2023. In this meeting, we discussed and demoed the latest features in the 1.2.0 Release. Watch the video to learn more about these features:  
\- Domains & Data Products  
\- Glossary Approval Workflow  
\- Data Insights - Cost Analysis  
\- Knowledge Center  
\- Personas & Customizable Landing Page  
\- Metadata Applications  
\- Performance Improvements  
\- JDK & ES/OS Version Upgrades  
  
\*About OpenMetadata:\*  
OpenMetadata is an all-in-one platform for data discovery, lineage, data quality, observability, governance, and team collaboration. OpenMetadata (https://open-metadata.org/) is an open-source project supported by Collate, Inc. (https://www.getcollate.io/). Collate also supports a \*SaaS version\* (https://cloud.getcollate.io/).  
Join us on Meetup to get notified about OpenMetadata Webinars: https://www.meetup.com/openmetadata-meetup-group/

## Transcript

### Intro

**0:03** · good morning good afternoon before we start quick we intro on what it is that we do here for the folks joining us today for the first time the goal of the community meeting is basically to have a uh a chance to touch base with every one of you here we want to give you some updates on how the community is behaving how the project is evolving and also have a space where

**0:29** · either other folks from the community can present their experience and their learnings and their use cases with open metadata and where we can also Deep dive into specific fees and specific pieces of the project for example we have done other webinars about the Data Insights

**0:45** · data quality the ingestion and if you are interested in also kind of learning more on those topics that we have already covered here please don't hesitate to go on YouTube and take a look at those recordings they are super super useful and without further Ado let's start

### Community Stats

**1:04** · digging into the community stats we have had 10 new open source developers since the last meeting thank you thank you thank you for everyone who's contributing here I always get excited when I see a new PR and actually this time we had a lot of good quality ones so thanks for joining thanks for chipping in we are also very close to

**1:28** · 3,000 stars for those of you who are here who like the project who would like to bump this number a little bit until we reach this 3K don't hesitate go into GitHub give us a click it's super helpful for us to make sure that we can easily spread the word we have also crossed the 4,000 Mark of community members in slack

**1:53** · for those of you also that you are not there yet this is the main and easiest Communication channel that you can have have with the rest of the people in the community and with us as well you can come with questions with fature request and we are there for you to give a hand to guide you to listen on what are your needs and make sure that your feedback can also become part of the project itself and finally together in I was

**2:20** · about to say Twitter but in X and in medium we are also very very close to the 2K Mark so don't hesitate to follow us as well to not miss any community meeting and to not miss any social update that we can give out in terms of contributions we had

### Contributions

**2:40** · anatol arum Christian for third or fourth time thank you for continuously chipping in we also have Joseph Kean Louie Mitchell Lo thank you very much for helping us improve ler it was great H working with you for those of you that do not know we have kind of a hard time

**3:02** · uh developing and testing look at we have a hard time putting our hands on an instance so all the help that we can get there is super super appreciated so thanks L for chipping it in here we also had prit Rio vanika blat volov and William thanks to all of you for your contributions Thanks for opening the PRS and helping us keep growing the

### Metrics

**3:25** · project in terms of metrics here you can see on the left the number of PRS that we merged per week so those are from September and the first week of October as you can see we had two weeks where either India team was off Spain team was off that's why you see these uh two big

**3:49** · actually like smaller bars on the sides otherwise we're in a very healthy position at around 75 PR that get merged every every week which is something really really great and that has helped that shape the1 to release to where we are right now and in terms of support questions I was talking about slack so we are at a very stable 100 questions being asked in support every week so if

**4:18** · you'd like to chip in you can also go you can help us answer any of the questions that are there because for us it's super important that all the threats get a resolution that all the threats get answered to make sure that we can all continue moving up uh with open metadata so all of these threats we jump in but if you are there you are a veteran in the community and you would like to give a hand to please don't hesitate to also participate on those

**4:48** · those discussions here and last minute from my end today we have a very very very special meeting because we want to show you all the amazing theats that we have been building for the release 1.0 we are going to be giving that out on the 26th of of October that's just next week and we have brought in 300 tickets and more than 800 comets since the release uh 110

### Theats

**5:20** · so a lot of awesome things that are going to be there and that we are going to present to you right now we'll be talking about domains and data products closer approval workflow the new introduced surge indexes and store procedures will'll also introduce some feates that will only be available for Cate for our SAS offering of open metadata such as the cost analysis and

**5:43** · the knowledge Center here you see green plume that was actually a community contribution so thank you very much for that we have also gotten some help to translate open metadata in German so if you'd like to change the language in on the UI to German to French to Portuguese

**6:02** · all of that is there German is going to be brand new so I'm going to stop here and I'm going to pass the word to sures who is going to talk more about how we have built and defined the domains and data products can you guys see my screen one of the biggest features we have added in um This 1.2 release is uh domains and data products uh so the concepts of domains and data products come from data right and one of the challenges is data

### Domains and Data Products

**6:34** · mesh is not an architectural principle it's an organizational principle and while domains and data products at a high level you know they're they are something that you know has existed even before data mesh right so people do understand it but implementing data mesh

**6:53** · the details of how to you know Implement and you know uh organize around it is is fairly vague and this is one of the reasons why you know we have slowly adopted some of these domains and data products one of the other things that we are also doing is while data mesh is uh

**7:10** · a much needed thing as an organizational principle in very large organizations for a small organization uh with small teams it might be an Overkill right so so adding the concepts of domains and data products without adding complexity for a lot of our users who are probably small teams and don't need that complexity is one of the challenges that we had to handle right so now just going into domains uh in

**7:37** · data M the whole idea here is um you know your your data team and the teams that are producing are large enough you want distributed uh data architecture right where different you know different teams and different parts of the organization are working within a domain

**7:57** · and the idea here is end to endend ownership right so in the past you would have you know somebody doing operational data and then there is a centralized team that is doing analytics data and it is trying to produce analytics data for the entire organization and it doesn't scale well you know it doesn't understand all the business aspects of the data because it is a centralized team so the idea here is you give endtoend ownership to a domain where

**8:23** · they have you know the services that are running that are providing apis that are writing to operational data and then this operational data is brought into you know the the data lake or data warehouse as raw data and then it is curated and then it is you know curated data sets and dashboards and things like that are provided as data products so your operational data the ETL

**8:48** · pipelines how you're you know transforming the data all of those become internal details of your domain and then the data product is what you're providing outside the domain for other domains to you use or even you know users from within the domain to use and so uh so domains provide data product uh

**9:07** · to the consumers of the you know the the data of that domain and it is based on data contract and you know uh open metadata has some amazing features related to data contracts where you have data quality test and slas uh which is coming uh freshness all of this is going to become part of data contract in the future uh we've you know same definition

**9:31** · that is provided in data mesh there can be three types of uh domains consumer aligned you know aggregate which is essentially a centralized team doing you know multi-domain stuff and then bringing the data together and then Source align where you know people are going to be consuming the data especially your you know data citizens right uh so we've added the concept of domain based off of this uh We've also added uh the concept of uh data as a product which we call as data product uh

**10:00** · data product is also used uh in the other context where somebody is using data and building a product is called a data product so uh within data mesh the this the term is data as a product but you know in short within open metadata we call it data product so it's a logical component that contains you know the data dashboards code maybe API

**10:22** · interfaces uh you know that serves uh the users right that are consuming products from a domain and it is owned by a team uh that ensures all the data gu guarantees right you know that there's data quality there's slas all kinds of stuff including you know uh documentation uh for the consumers and understanding you know uh consumer use cases and building the data product based on the consumer use case which is a shift in Paradigm where you know the

**10:52** · the data Engineers would just you know get some requirements and they don't think about who the user is what their use case is and they just just you know uh transform the data and provide some curated data sets here the idea is you actually think about your consumers their use cases and build the data product which could be your D dashboards

**11:12** · uh it could be your uh tables that curated tables but you understand customers use case and continuously improve the product and provide some guarantees like you would do for any other product for data um few things uh within open metadata uh in a domain uh you know the data assets tees glossies and many other kinds of assets can be added to a single domain right uh so you have clear boundaries of

### Data Products

**11:41** · where they belong and so data assets cannot belong to multiple domain a domain can have zero or more data products so if you are a company that wants to you know provide data products you can provide data products as a domain or even you can provide data products independent of a domain uh domain is inherited so if you go to a

**12:01** · database and said this database is uh belongs to this domain automatically the database schemas and tables and stall procedures under it automatically inherit this domain so you don't have to go tag each of the asset with domain you can tag it at the much much higher hierarchical level coming to data product a data product is made of one or more data assets you can just have one dashboard and call it a data product or you can have multiple um dashboards like

**12:28** · you know for example customer churn you could have customer churn monthly customer churn yearly right customer churn by region customer churn by demographic all of these different um so you can have you know different kinds of customer churn dashboards group them together into a customer CH data product right um a data

**12:48** · asset can be part of multiple data products right so if a dashboard is relevant to multiple Dash data products you can add them into multiple data products and then the way we are approaching data product is if a domain is hiding all the implementation details and providing data product as something that is consumable to their you know users data product is a public asset right uh that means and I'll go over this U you know later during the demo uh

**13:17** · a data product is a you know public asset that is discoverable even if you have you know domain only view uh that you're using our own recommendation is if there are you know ET and pipelines and things like that that are pro providing producing the data product that should be an implementation detail within a domain uh you provide you know only what is consumable by the users as data product so that you are not um you know confusing them with all the implementation details which is totally unnecessary right uh so quickly going to

**13:50** · the demo uh the first thing that you would see is um we have introduced uh a menu here uh which is you know uh for you to access all the domains and you can Define different kinds of domains what we've done is um unlike data assets

### Demo

**14:07** · where the descriptions are much shorter uh domain documentation can be much larger including you know talking about what the use case is and what is this is built for all of the description can be provided so we have a separate tab for documentation so that you can have Rich documentation um we are also provided within a domain you can have a domain owner uh and then experts within the

**14:30** · domain uh this helps in collaboration right you have provided some uh you know products within the domain uh anybody has questions they can get in touch with experts we have also provided domain type um we'll you know get your feedback on if you need to add different kinds of domain type beyond what is defined in data mesh okay now within a domain uh

**14:53** · you can have data products right so here is uh examples of data products and these are some things that are made available for the users uh now your product availability right and you can have Rich documentation again here you can add experts here for the specific product and you can have multiple you know data assets here uh that belong to this product availability right and you can provide all the descriptions on how to use it and how this provides data uh you know the product availability uh related information so that is um um the

**15:26** · data products and then going back to uh the uh the the domains you can you know whichever you know wherever you're you know either tagging at the leaf level or a much higher hierarchy all the assets

**15:43** · that belong to a domain are listed here right so uh so these are you know internal assets within a domain and this can include everything right everything from tables to dashboards to pipelines all of those things are part of the domain and those are listed here and you can browse them um so that's uh the

**16:05** · domain view the other thing that we have added is um the concept of domain only view so let's assume that there is a data scientist who is working within let's say marketing domain uh today in open metadata we have a flat view of all

**16:20** · the data assets available within an organization and you know this can be overwhelming right now somebody who is in let's say a marketing domain can actually go into the marketing domain only View and can now look at only assets within their organization uh so this is a starting thing that we are doing we'll continue to provide domain only view for data quality and you know

**16:46** · uh Data Insights and stuff like that which now you know gives you the view within your own domain without having to just look at the entire scope of data within an organization right so that's the other thing that we've added so we will um have our Beta release that will come out and U um you know you can U um

**17:09** · play around with it and provide feedback uh one last thing that I also wanted to show you is so the the inheritance of domain so let's look at this uh where in marketing domain there is no databases right so there's already domain only view so I go to shift and you know there

**17:30** · is this database now I can set this as hey you know this belongs to engineering right uh once you do that uh what is going to happen is the domain is propagated to the database uh you know

**17:46** · tables uh schemas everything under it right from that hierarchy so you don't have to set domains at you know every asset level you can set it higher up in the hierarchy right so coming back so this is just the first iteration of domains and data products and we believe there are many things that we still need to do uh we will add

### Coming back

**18:07** · in our backend we support subdomains but we wanted to slowly introduce this feature so we'll add the concept of subdomains and that way now within the domain you can have you know subdomains that specialize uh you know on certain things within the domain uh the second thing that we want to also will be doing is uh domains and data products and are you know as independent entities from each other so today data product can only be created in domain uh which is fairly you know very closely tied to how

**18:39** · data mesh defines it but we believe that there are organizations that want to use domains there are organizations that want to use data products independent of each other so uh this will be uh you know this feature will be provided and then you can tie a data product into a domain right uh as I said we will

**18:58** · introduce domain only view of data Insight so if you just want to look at uh what is going on in marketing domain and how the data assets are growing how the usage is uh that will be available in the next release uh domain only view of data quality what is the data quality within a domain and uh how are the you know what are the tests that are available and how are they failing that will be available also uh the other thing that we will introduce is ability to turn off domain and data products if you're a small company and you don't want to have this complexity uh in open

**19:31** · metadata you should be able to turn it off and then iteratively incorporate Community feedback now this is very important for us because data mesh is fairly high level Concepts there is no clear description of um how it should be

**19:48** · implemented and every organization is implementing it in different way uh hopefully together as a community uh we you know you know we continue need to develop best practices and then adapt based on that Community feedback into what we have built in open metata now the other cool thing that we have done is glossery uh approval workflow uh so you know glossaries is

### Glossaries

**20:12** · something that we are continuously improving and um one thing that we have done is and I want to call out you know a lot of contribution from doel on this uh we have introduced um styling for glossaries so you should be able to um go to Glasser terms and uh you know

**20:32** · you should be able \[Music\] to style the glossy ter you can actually you know for a glossy ter have a separate uh icon if that is how you want to differentiate uh you know and and group the uh glossy terms you can also pick different colors now this is a first iteration um you know I there is a

**20:53** · lot more that we can do here so you can set colors and and these colors will be available wherever you have used these glossery terms for labeling labeling your tables and columns and all of those things that way you can visually differentiate between them uh so that's uh one of the cool features that we have added and you can look at different you know color coding right here um and color coding you know one of the use cases for color coding is maybe security is a type of a um you know um glossy

**21:25** · term related to security operations things like that can be color coded um you know similarly now you can actually understand what this color means and what you know classification or a category it belongs to uh so that's the preliminary use case that we are starting with right the other thing that we've also done is uh the glossy approval workflow uh so the way glosser

### Glossaries Approval Workflow

**21:49** · approval workflow works is uh you turn on approval workflow for a glossery by setting the reviewers right if you don't have reviewers set for for a glossery any term that is added is just added in an approved state but if you have set reviewers for glossery any new glossery term created will be in draft mode right

**22:09** · and then a task is created for glossery reviewers to approve the term right uh only a reviewer can approve or a reject a term right um you can have conversation around this task saying why it was rejected why you know if there is any change further change is required before it can be approved just with all the you know cool things that we do with conversation threats uh one of the things uh that uh you know this feature does is only reviewers can approve from draft mode to approved mode not even admins can do it so that you have uh

**22:42** · tight governance control on what terms are being accepted right um and then you know this is a starting point for approval workflow right we are only doing it for draft to approv mode there are various States a glossy term can go right from approv to deprecated maybe

**22:59** · approv back to draft and stuff like that uh we would like to get your um inputs on what other kinds of approval workflows and what improvements can we do with the current approval workflow so let's take a quick look at this I have created um uh a uh a term let me add also another term

### Glossaries Term Approval Workflow

**23:22** · and then I say this is test three um and then I've added this and because this glossery has reviewer Set uh this glossery term is going to be created um in draft mode right now if you go here right um I am one of the reviewers and if I go look at this uh what happened so this is test one okay I click the wrong

**23:55** · one let's go to this ah test one is in draft mode so okay so test three was created I can actually just appro it and then it goes into upo state so only reviewers can approve it there also you can track these tasks as a reviewer by going to um

**24:19** · you know your um tasks and then here you can actually look at you know all the tasks that are assigned and then you know you will have approval task here right somewhere this one is uh so this one is already done uh so if you have an approval you know task you can also you know approve or reject it you can track them as

**24:43** · tasks uh against your personal profile right so that's uh glosser uh term approval workflow again we are starting the Journey of different kinds of workflows for governance purposes you're allowed to get your feedback more over to the next

### Search Indexes and Procedures

**25:02** · presenter awesome thanks Sur for the information so the next topic that we have here is actually how we have introduced the concept of the search indexes and the procedures so if we go now into settings and take a look at our services I will start by showing you the indexes that you can now pick up

**25:26** · from elastic search so if you were curious about how we are defining the mappings the types of the dogs that we have in the open metadata elastic search you in lack you can just point here and get all the information but before we get there as you can see the service view has also been updated so I can show this one for the databases because there's a bit of more content so by default we will show this list view with a description the type and the owner on each service and what it's going to be super useful is that you can now bulk

**25:59** · deploy the ingestion pipeline so let's imagine that we roll out um a new release maybe we changed H some of the inter internal details and in the docs we ask you hey please let's redeploy the Ines pipelines you can now just do that in bulk directly here from the service list then if we go back into elastic

**26:21** · search you can see here some filtered indexes that we inject Ted from our uh internal elastic search and if I take a look at the table index you can see how in the fields we're going to show actually everything has that has been defined in the mapping we can come we can update the description tagget at the glossery terms your typical Suite of operations that you can do for any entity we are also going to be bringing

**26:53** · in any sample data in case that that might be interesting for you to further explore on the UI as well as further information about which analyzers you're doing normalizers any specific settings that you have set in the index so this is right now available in the one 120

**27:14** · beta you can go you can take a look you can try to ingest your elastic search or open search sources and do let us know if you have any questions or any feedback the other interesting entity that we added is actually the data products and in order to discuss that a bit better let's imagine that I have one database that I call Silver one database that I call Gold and that I have some table users that I'm transforming from

**27:46** · my silver database into uh my gold database and that this transformation actually happens with the store procedures so here at the schema level you can either list the tables or the stor procedures and if we take a look at which kind of information we pick up from them you're going to see that if those store procedures are defined in Python you'll see the python functions

**28:12** · if those are defined in SQL you're just going to see the SQL definition and directly from the metad ingestion if this store procedure actually helped me move my users table from silver to gold we are going to be seeing that lineage as well and as you know if you take a look at the lineage here in this case

**28:34** · the store procedure for us is an edge so if I'm taking a look at the lineage directly from the edge the same what happen with the pipelines you will see these little box explaining what's the code for my procedure what's the language and any other information that I have shown but I can also go directly

**28:51** · into my table View and if I take a look at the lineage I'm going to see this information directly encoded in the edge I'm going to see the exact query that was triggered by the procedure and how this query populates this case I just have a simple select star so that just populates the column level lineage from entity to entity before continuing with this example of store procedures another great Improvement that comes out in the one to Z release is actually in terms of

**29:24** · the Chrome extension you know that in the latest release we did a very amazing update from part of the UI team on The Full Experience the full look and feel of the platform so now these changes have also been applied into the uh Chrome extension so you can take a look at all the activity feed you can take a look if you have any mentions if you have any pending tasks uh at your name

**29:49** · but not only that we added support in the Chrome extension for other entities as well because before we supported pipelines we support the dashboards and now we support absolutely all the entities so I can come back let's see where do I do have this is my great

**30:07** · start procedure so let's imagine in this case I'm just directly jumping from the open metadata UI but let's imagine that I'm just exploring my data directly in Snowflake and I want to validate what this means how this is used directly from the extension so I can come click on my extension and I'm just going to see the

**30:30** · owner we will also be showing the tier we'll be showing the domain we'll be showing any tags any glossery terms any descriptions as well as any lineage information about the other entities uh that are involved as

**30:47** · well then we can continue going with the rest of the demos where Teddy it's going to be talking about the cost analysis thanks for those great demos very and andar that was a awesome and super super exciting um so as you can see we had earlier logo change right here uh so here we're going to talk about a a feature that is available in

**31:17** · the colas offering uh so if that's something you're interested in uh feel free to reach out and and we'll be able to to discuss um but as um as you probably know or if you're new to to open meta data today uh we provide uh some data Insight inside the platform so with the data Insight you are able to understand the composition of and the structure of your data platform seeing how many assets you have by categories um and get a bunch of

**31:52** · um different information around description ownership tagging and and and and usage St of uh open metadata um with that iteration and that release we wanted to go to go one step further um so as you've probably experienced and as you know we we we have experienced in our previous um um in your previous in

**32:14** · our previous roles um often time and you may discover that with open metadata inside the catalog you can have a large amount of data set that are unmanaged inside your or organization right so browsing open metadata you can discover specific asset that you didn't necessarily know existed or or we here right and so what we wanted to provide with that metadata information available inside um inside open metadata was a way

**32:44** · for you to actively manage those assets right so in in the 1.2 release we're bringing that information starting with uh snowflake specifically and then we'll be uh spending it to other data assets other data sources where you'll be able to see and understand um when was a an

**33:06** · asset last use right so when was that asset last access what's the size of my uh data asset and then we be also uh providing uh the the potential cost uh for your organization of your asset in the um in in the next relas right so um

**33:27** · today for people who are um either customers of colate or who will become customers of colate um in the future when you navigate to the uh data inside tab you will see a a new tab under the

**33:42** · free existing one that you may be familiar with um with the open source uh um tool which is C called cost analysis right and this cost analysis tab will give you some important information around your your ass ass usage right so we have a few graphs that are available the first one being the count of assets

**34:04** · um that are used versus unused right so you're able to see a um a Time series representation of that of those asset and then you are able to similar to how you can navigate with the other uh graphs you are able to filter for you know use and unus and that allows you to see okay in my platform how many are used or unused data set do I have right and so this information will be uh defined as last access in the in the

**34:34** · last three days for use or unuse and then you able to see it at a different um um time breakdown right and then similarly we provide um a a view that will show you an the same information

**34:51** · but mentioning the size of your use versus a use asset right so you may have a small count of unused asset inside your organization but that small count may represent a large amount of data storage which potentially would have a great impact on the cost of storage and whatnot um inside your your

**35:13** · organization and then the the third graph will uh show you a similar representation but uh over a St graph so that you can see the representation of US versus a new similar in terms of of count and in terms of percentage and then finally we will be providing tables that will allow you to drill deeper into which assets have not been used uh What

**35:38** · uh when they when when were the last access what's the size of those assets and whatnot so for example here we can see that we are looking at assets that haven't been accessed in the in the last three days and then I'm able to you know ex extend that range and say I just want to I consider assets that are you know

**36:01** · important to maybe clean up inside my organization as asset that haven't been used in the last uh 30 days and then I will have the list of those assets with the size and how much stories do they represent inside my organization and then from there I'm able to actually take action and actively manage those assets inside my organization and similarly I have a view that will show

**36:27** · the frequently used asset right so those are the assets that have been accessed um at a specific frequency that you can uh choose and filter by uh right here so basically with those uh those those added View and that's a view that we will keep iterating on adding more assets adding uh additional filters making it even more actionable for you as a user you're able to not only you

**36:56** · know see the the structure and the composition of your data platform but you are now able to actually take action actively manage your asset inside your organization and make a difference right so save cost for your for your team for your department for your um for your organization all right so with uh with uh that I will uh um pass the um well

**37:23** · pass my turn to to Hara who will be presenting the the next topic all right thanks stud so if I'm going really fast it's because per told me I only have off the time so pardon me if I'm fast going really fast place so

### Knowledge Center

**37:40** · with this release uh we're shipping Knowledge Center as a brand new feature so if you're using open meta so far you must be familiarized with our Rich markdown editor right it gives you amazing ability to document your data assets tables topics pipelines you can embed image you can write really nice documentation explaining what that data is about but with organizations you

**38:01** · often get a need for kind of documenting about data itself what are the best practices to use the data what are the naming convention you should be creating while you know creating an asset how the data infrastructure works so these are the articles that really useful for the users to understand how the data functions in an organization with knowledge sender we are bringing a brand new functionality into open metadata where you can add full page articles describing you know how the data works Works what are the best practices so that you can educate users of the data

**38:30** · right within open metadata so let me jump into the UI you will see new menu item called Knowledge Center you'll see list of articles that are being set up for you right for example I have onboard your data you can

**38:50** · see amazing this page where you can really clearly articulate bring in your architecture diagrams images whatnot a full Place full length article for users to discover and understand the data typically organization do this bya Confluence or Google Docs the problem with that approach is as a data user I come in here I Discord the data assets I can

**39:12** · understand what the documentation about the data Assets Now if you want to know a little more about it I need to jump into another tool now we are bringing another tool that's not required in your organization right within the open met dator so as the data user not only understand all the Met all the data in the organization I can also understand what to do with that right for example it's my day one at my company what should I do you know go visit this article understand what's happening in your data and every feature that we

**39:39** · develop with in openm data all the amazing base features that comes along with it for example you can vote up and down you can look at the version history of this uh this page right you can also follow our bookmark dis page you can share the link you can also add comments and have Rich description uh conversations around this article so and with this uh feature we are also adding a brand new editor for example I want to do day one Ed right now I can go

**40:12** · and hit slash I can get all my formatting options not only that I can actually add a team tagget right or I can add something uh you know table or reference to any entity within open meta so you can build amazing articles with this options not only that you can also add quick links so that if you want to share certain you know predefined arure diagrams or everything else you can build all of that within open metadata

**40:40** · so this is great new feature that we are super excited about um I'm sure you know you get a chance to go to the sandbox beta play around with it give us feedback and you know give us kind of informed about all the features that you're using so that's the knowledge Center I'm going to go into the next step which is personas and customizable landing page right what is Persona in a open

### Personas

**41:03** · meta world like for example if I'm an engineer at my company I'm a data engineer I deal with pipelines I deal with data quality test I deal with onboarding new data assets whatnot but I'm also a an engineer who's been with this company for a long time so I develop a lot of um internal knowledge T knowledge about the data so I can also play a role in the data to manage

**41:26** · governance or glossaries to help other users and so on so for my day-to-day I want to use my open m data using my data engineer role but I also want to kind of log in and kind of test you know how the governance is going on how to I approve other gloss returns and so on so these different personas we want to support those personas within open meta so what

**41:48** · does that mean right so how we can actually tune fine tune the open met data for the person that you're logging in with that is one option with going forward with Persona we want to bring in a lot more functionality for example maybe a roles can be associated with Persona so that when I log in as data engineer the application behaves in certain way when I log in as data stward

**42:08** · uh the application behav in a different way based on the confutation associated with Persona and one of the first application that we are building on top of persona is customizable landing page right so if I go back again to the my landing page here so this is a familiar landing page we already use open met data we have different pan that gives you more relevant information about what you're doing in the open data

**42:31** · there is activity field that gives me all the activity that is happening in there is Task there is recent announcements following anything that I viewed recently so on these are all the panels but this experience is very common for every user right so with personas as an admin I can go here click

**42:47** · on the personas I set up already a data engineering data STS dat senters in this case and I can add a Persona new persona too so with that I'll just going to the existing Persona you can associate users for a given Persona so once you set up your personas now you can go on to the open metadata customized landing page you'll see the same personal that you set up previously and here you have a customized landing page so I'm going to go and change customiz landing page for

**43:15** · data scientist for example maybe I don't think key performance indicators is useful so just to reiterate this is the landing page that you see when you landing on the main page now you can actually configure here I want to put my recent announcements at the bottom of it right and to keep my recent views so that I can easily access here and I want to kind of remove this key performance indicator here and add a different panel

**43:42** · this is the most cool thing so all these things comes as panels right now this is a plugable panel implementation the UI and back in working in tandem to deliver a single widget or a panel uh that can be comfortable in the landing page right for example in this case I want to maybe add announcements again here right so there is a new panel added now once I'm happy with these panels I can hit save

**44:09** · right I can go into my landing page you see the same landing page here previously that we have seen as user I logged in and I have two personas that I have I'm going to change to data scientist now everything else is changed as per the configuration that we just did just put recent announcement here you put the recent views at the top all this layout is changed based on the Persona that I Chosen and as a user I can also select hey this is my default Persona so that I don't need to keep switching it all of these things coming in release 1.2 and the great thing with

**44:41** · this option is we will continue to keep adding new knowledge panels for example we want to deliver a pipeline statuses as a knowledge panel right so as a data engineer I can add that uh panel into my landing page as soon as I land in I get my latest statuses similarly data quality lining uh knowledge panel and so on and going forward we want to kind of also customize the entity Pages as well for

**45:04** · example in products page maybe you can add knowledge articles panel here any articles that associ with products will be visible right here so there is lot of customization lot of interesting feature that we can deliver on top of personas and customizable landing page now open Med is much more customizable based on the the Persona based on the function of the user who logged in

**45:28** · right I'm going to go to this is my one of the you know favorite features of this release I know it's hard to choose your favorite child but I'm doing it so met application I'm super excited about it why is that so when we announced open metata back in 20121 August itself we set out a vision a grand vision of data

### Metadata Application

**45:46** · Discovery data collaboration data quality observability and importantly automation we kept saying that once you collect the metadata there are lot of job functionality lot of things that you can automate about the changes that are happening in the metadata so we bu what

**46:03** · we build so far is from the very beginning itself we have metata change events any change that is happening in Source like you know snowflake someone change the schema uh someone come to the open metata they change the description tax whatnot you get a metata change event you can react to it so for that

**46:19** · automation is hey create a web hook link you can receive this events do your automation what you want to do there but with this brand new feature what we are doing is building a framework for you to actually build an application that can run within the open met data server you know analyze the metadata that is happening within the open metata are from the externally from your sources react to metadata change events are the metata that is already collected build automation that can periodically execute certain Auto functionality and endr metadata endr data that you are operating on we built marketplace where

**46:52** · there are list of application that is available today admin can install of these applications today right so to demonstrate what we are building as a first step we took the familiar application that is kind of bed into open metadata into a plugable

**47:07** · applications so go to the settings you'll see the Integrations here there is applications right now I have Data Insights and Data Insights report as my application that is already installed so if you're again familiar with open m data you know Data Insights is a pipeline that collect all the insights

**47:24** · that t was showing just before and you know gives you a data Insight reports and then there's a data Insight report that sends a weekly email or a you know conf period of time to Showcase what is the health of your metadata what are the kpi that set against organization where are you with the ru

**47:41** · now I can also add other applications once I click add applications you see you know these are the two application that we already installed we have search indexing search indexing is a way to kind of reindex all the metadata in case of you know you want to get latest uh index mix ing off all the material that is happening here go hit read more we

**48:00** · will be enriching these Pages as we coming closer to G of this release I can see that this is developed by open materal itself you know all these DET different details and also click install once I go to the install it says okay searching is in application by Cate

**48:17** · and it's asking for all the metadata because it needs to you know look at all your metadata to index into elastic or open search based on your configuration so you know what it is accessing it I'm going to click configure here it shows this particular application configuration so each application will come up with their own configuration and it says okay I'm going to index all the pretty much entities here I'm going to use the sear IND language of English and I'm going to recreate the indexes when I'm indexing it right once I submit it

**48:46** · it also gives me an option to schedule it I'm going to schedule it every hour submit and there you go we install an application that is an external application to be run within your open data server at a periodic time that is you configured once you go in here you can see okay schedle type is this it's supposed to run every hour if there is any history of runs you can see here and here is a configuration that you can again update change it and I can hit run now for on demand

**49:17** · run and it is running right now and once the run is finished you will have a lock as for now what you have seen so far is and framework that allows you to build these applications all of these applications it comes with a manifest GSM saying that hey I'm an application

**49:35** · I'm going to install in open meta server I'm going to run externally as another pipeline uh just like our service pipelines and you will clearly know what the metadata is accessing it and you'll get an option to configure it you can schedule it and deploy and install it once you install it runs periodically every time every hour now imagine the possibilities as we go along on this journey the kind of application that we get to create we get often I think even today asking hey can we propagate tags

**50:05** · this this could be an application right you can use lineage propagate the description tags of a column or a table all the way to you know dashboards and reports that are being generated based on those colum and tabs that could be an application that can be scheduled at a periodic times look at the metata that is happening look at the lineage events and propagate this uh description taxs

**50:26** · this could be a life cycle policy just like we showed in cost analysis report if there's unused data you may want to delete our you know rename the tables and record the cost of hosting the data right now you can build an application saying that hey if a table is not access in the last three months maybe we should put a tag around it and garbage like the data in the snowflake red shift arbit qu so all of those applications can now built in and shipped as a Marketplace

**50:53** · installed for all of these users so that's the power of automation within the open metadata and we're just getting started in shipping this amazing new applications so here is logs how it looks like you can have a history of all these runs and uh look at the audits of these applications as well so that uh covers my quick

**51:15** · roundabout of all these three amazing new feature that we shipping and you know um we just getting started on these Imaging new releases with that I'm going to give it back to like thanks for explaining super excited about the application super excited about the knowledge Center super excited about the cost analysis know that Knowledge Center and cost analysis are going to be only for Cate if you would like to try those out they are right now

### Performance Improvements

**51:44** · in the sandbox beta we also make them available in the sandbox and if that's something that you would like to bring in into your organization don't hesitate to visit cloud. C.O you can send in schedule a call with our team and we give you more information about this as offering but before we finish two more

**52:05** · updates on open metadata itself the first one and we are super happy about it is that we made a bunch of performance improvements if you'd like to dive a bit deeper into all of the needs and bids and the changes that we did in there we are just uh linking here the issue but in a nutshell we reduced database trips we cached some of the information that was frequently looked we stored some summary data just to make sure that the UI can load faster we also

**52:35** · rebuilded the indexing and de colation of the databases and we also scheduled an internal benchmarking process to make sure that release after release week after week we are in track with our performance goals and these changes actually gave us an more than a 90% decrease in the resp response type for certain right operations it also increased uh the the efficiency of the lists and the gets so you will see how

**53:05** · in 1.0 open metadata will be blazing fast and here it's just small screenshot on how this performance report comes to slack just because we are super proud of it we'll keep monitoring these results we'll keep checking and ensuring that the performance only goes better better and better and finally some more considerations and changes for you on this release is that now the open metadata server is based on Java 17 so

**53:37** · you can upgrade uh your services with that and most importantly elastic search and open search clients we now support up to versions 8 102 for elastic search and 2.7 for open search so in one to

**53:54** · feel free to upgrade your server upgrade all of these dependencies and enjoy all of these new goodies and theaters that that are out on the one to release and that's actually all from our end uh not

**54:11** · even sure if we were able to have uh some time for for questions so please don't hesitate to start the project on GitHub you can check out this we didn't change to X please check out as out on x check the colate page check uh all the

**54:29** · conversations and the discussions that are having H that are happening in slack and please join us so if there are any pending questions you can use uh the chat otherwise maybe K Sur we can stick two more minutes for one Live question five more minutes if there's someone that has anything to share so I got a a use case question so I'm new to open metadata we have a use case where we

**54:56** · have a similar database schema across 100 or so clients um and that that's that scheme is in a postgress database if we want to manage so we can import all those as different databases um if we wanted to manage metadata across this metadata I guess like add labels and tags and things like that is there a good approach to that

**55:20** · like how would you suggest tackling that this is definitely a long discussion but you know there are several ways um to solve this problem and uh and depend it depends on what you know requirements you have so concept of you know there's a logical schema and there are lots of physical you know representations of it

**55:42** · in some cases it's a logical schema but the you know the same logical schema but the data is different right so you know in in in in in those cases you have to have data profiling and all of those things that are completely separate you know for every database so um so I think

**55:59** · you should be able to write U some kind of a uh application yourself right um where you know you take one of the schema as a master schema for applying descriptions and uh tags and stuff like that and when something changes there you can go back and apply everywhere else if the data is just using the same schema but the data itself is completely different yeah right but so and that

**56:24** · should be fa easy to do with the apis great um and you may have said this earlier when is the the new is the application stuff available now or is that in a beta or coming soon you don't even need to wait for the writing this application you should be able to just you know today you should be able to write some scripts that take you know this tags from your you know one copy where you're maintaining it and apply it across uh all the others yeah that makes sense okay cool

**56:54** · thank you perfect if there are not or if there are not yet you can sleep through the content rewatch the webinar uh if there are any questions that arise later on please feel free to join this slack

**57:12** · feel free to reach us out and we'll be more than happy to continue any discussion thank you very much for the for the attention thank you very much for your time looking forward to see all of you in the next community meeting thanks