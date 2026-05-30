---
title: "Mini-Webinar on Custom Connectors #dataintegration #connectors #ingestion #datacatalog #metadata"
source: "https://www.youtube.com/watch?v=fDUj30Ub9VE"
author:
  - "[[OpenMetadata]]"
published: 2023-01-20
created: 2026-05-14
description: "Pere Miquel Brull will discuss some of the core aspects of OpenMetadata, the ingestion process, and will showcase a demo on how you can build your own custom connectors in OpenMetadata. Thanks to the"
tags:
  - "clippings"
topic:
type: "note"
---
![](https://www.youtube.com/watch?v=fDUj30Ub9VE)

Pere Miquel Brull will discuss some of the core aspects of OpenMetadata, the ingestion process, and will showcase a demo on how you can build your own custom connectors in OpenMetadata. Thanks to the custom connectors, you can integrate your internal business systems with OpenMetadata, and explore their metadata together with the other third-party services crucial to your business.  
  
What we’ll cover in the Mini-Webinar:  
\* OpenMetadata Foundations: Schemas and APIs  
\* How this translates to the Python SDK  
\* How does the ingestion work  
\* Demo on implementing the Custom Connector  
  
\*Webinar Slides:\* https://www.slideshare.net/slideshows/openmetadata-webinar-on-custom-connectors/266190084  
  
\---  
\*About OpenMetadata:\*  
OpenMetadata is an all-in-one platform for data discovery, lineage, data quality, observability, governance, and team collaboration. OpenMetadata (https://open-metadata.org/) is an open-source project supported by Collate, Inc. (https://www.getcollate.io/). Collate also supports a \*SaaS version\* (https://cloud.getcollate.io/).  
  
Join us on Meetup to get notified about OpenMetadata Webinars: https://www.meetup.com/openmetadata-meetup-group/

## Transcript

**0:00** · and that being said we go into the webinar side of things for this community meeting and as we said at the beginning the goal of this one is actually to explain and into type a bit deeper on how you can set custom connectors into your own open metadata

**0:19** · deployment but before that for those who are new or for those that have already been with us for a while but maybe are not that aware on what are the foundations of open metadata let's do a quick review on two super important topics that are actually the ones that enable us to work on these custom connectors the first one is the open metadata standard right in the end here we understand each other because we all try

**0:49** · to speak and have to speak in English right we have this common language we have this way of sharing information with us so this is actually the same that happens when we are talking about software systems so in open metadata we are not only releasing this metadata uh

**1:10** · this metadata management platform we are also building it and releasing these open metadata standard the idea is that we have a way to define all of the assets that interact in a data platform these databases V tables dashboards be

**1:27** · the actual physical service that is the one providing uh all of the tables and here for example we are already unanswering questions such as okay what does it mean for an object to be a table it needs to have a name it needs to belong to a schema it needs to have some

**1:47** · columns then these columns can have a series of supported data types and so on and so forth so we are putting not only the descriptions but all of the validations and their types and all of their possible relationships from asset to asset and actually in what makes uh open with

**2:06** · a written interest in here is that we are not just stopping at the asset itself because we want to bring and to close the collaboration gap between the data side of things and the people side of things so in the same way that we can Define what a table is we can also Define what are those relationships with

**2:26** · folks that are part of the data platform so a table can be owned by a user then this user can be part of a team it can interact in some discussions in the threads and so on and so forth and all of this information lives together into the open metadata standard

**2:47** · then once we have this language we are actually able to see okay now I'm in a good place to go into all of these different metadata sources and integrate them into open metadata because in the end a relational database it's just going to give me a partial view of the information a data warehouse it's going to give me another side of the story The ETL it's what links all of these movements together but they might not be

**3:17** · sharing the same definitions they might not be showing the same descriptions and the same connections and the same apis and the same interactions so if we try to just get all of this data in isolation this is going to get really really hard so what we're trying to do with open metadat is to create this Central piece that's going to lie in between all of these Integrations in our source of sources of Truth and all of these possible applications that we can make once we have this metadata properly

**3:51** · defined with names and surnames and with a set of operations powered by the apis that allow us to say hey now we can create a catalog which is the one that we are shipping to allow you to collaborate to allow you to discover this is also what is powering our data

**4:08** · profiler and Quality Tool this is also how we are defining these specific reasons tests that are part of the observability of open metadata and so on and so forth once we have these integration once we have these apis once we have this language we just need to keep building on top of this based on our needs now that being said we have some Source

### Company Context

**4:36** · systems we have open metadata in there integrating all of this information I have this single place to go discover collaborate see everything that's going on with my with my data platform but in some cases that's just half of the story

**4:52** · this works when we have some external systems that we already know how to connect and how to interact with maybe I have some tables in Snowflake and these tables I spice them up with some DVD Transformations and they at the same time generate some new tables then I can visualize with metabase and all of this is orchestrated with airflow in the end all of these tools here all of these tools on the right hand side are the tools that are generally available in the industry so those are tools that we

**5:23** · as the open metadata Community we can come integrate with the tool Define all of these connectivities Define this transformation process from what the metadata looks like in the solar system and how I can translate that into the open metadata standard and send it to the server that's awesome but what happens if inside our organization we we have some specific business needs that

**5:49** · are only applicable within our business within our team even those are those internal systems there are still places where metadata is important that is important to be shared and it's important to be seen in this holistic more General View and together with the rest of our data platform so

**6:09** · what we are going to be looking at today is how we can close the gap between these internal systems and the other external ones that we already know how to give and how to bring inside open metadata so how do we bring it how do we close with this Gap how we create this communication with other Solutions and open metadata the ideas that we have

**6:35** · different solutions and not all of them are going to be giving us the same benefits and not all of them are going to be working in the same use cases so what we're going to do now is we're going to explore all of these different approaches and in the end we're going to Deep dive a bit more into how you can create a custom connector that's one of these possible approaches but if we try to look at them a bit together we can see that on the left we have API

**7:06** · calls we said that everything is centralized with the apis we have said that everything is focused and founded by these open metadata standard so we can directly use these API calls to interact with the server and for those of you that might not yet be aware of that everything that you do in the open metadata UI that's an API code so absolutely everything can be automated with API calls directly in the in This

**7:36** · Server what's the benefit here we have all the flexibility in the world as long as it's something that it's supported by the server we can just do this API call and get on with it watch the maybe not so moved but out of that that we really need to know what we are doing we really need to know what's this language we really need to know how we can exchange all of this information okay on the other side of things we have

**8:03** · the ingestion framework this is the python package that we have been developing in the community that we have been developing as part of the uh open metadata project that is the one that helps us connect to the sources understand the origin of the metadata then do the translation into the open metadata standard and finally send all of these into the into the open metadata

**8:28** · server so what's interesting here is that we already have a lot of boilerplate we have a lot of world Trails we have a lot of processes that are already based on all of these Logics so we don't need to do as much work but this means that we need to be in a position where our needs align with the abstractions and with the processes that the ingesting framework brings so let's go step by step and see these different examples and how would they look like

### Creating a Table with the API

**9:01** · this is a sample column how I can actually create a table with the API I'm just running a put pointing to the open metadata server as always we are sending here the JWT token for those of you that might not know that yet this token you can actually get it from the Bots page you can either use the token from the ingestion bottle you can create your own Bots with specific scoped permissions that then can maybe help you rely in a

**9:33** · bit more secure way for uh for different applications and here I'm just creating a super small table it's only going to have a name it's only going to have a column and it's not going to happen on it it's not going to have a table type and I'm just passing on which database schema this

**9:54** · table belongs to this is fine this is great this is all games but here the question is how do I know that I need to pass the name or how do I know that the table type can be normal it's some information that if I just want to use the API Pro I will need to check either by validating the Json schemas either by going into the Swagger dogs but I don't really have any

**10:22** · helpers here to help me understand okay maybe I'm just doing a typo maybe I'm just passing a data type that it's not properly supported and so on and so forth so if we go into pros and cons the price will be hey there's close to no requirements as long as you have portal or as long as you have any library that lets you interact with API calls you can already start automating things in open metadata the con will be that you really

**10:53** · need to know what you're doing you can go into Swagger we have a bunch of examples in there but building all of these jsons for pigtails for big pipelines it can end up being a bit purpose and we don't get some of the validations when we are actually playing with the code and deploying it in the middle in our graph at the beginning we have the python SDK and the

### Creating a Table with the Python SDK

**11:21** · Javas Decay I like python a bit more so here I'm just going to show you folks the example about python but it will be very very similar if we go to the Java site so here in this example what we're seeing is how with this SDK we can create a connection to the open metadata survey again we are just passing the port and the jwp token and based on this connection now I'm

**11:50** · going to create this create table request object and as we can see here we are already talking about different things I not just creating a Json file I'm creating an actual python class and this python class is going to support some arguments these arguments are going to need specific types that are going to

**12:12** · need to be fed from specific other classes so in this case I know that I need to pass the name that I need to pass this database schema that looks like it's another object called entity reference and here when I'm passing the columns I'm passing something of type column and I'm passing a data type which is of type data type what it's interesting here is that all of this information all of these validations can already happen on the python side of things I don't need to wait until I run

**12:44** · the API call on the server cries by is just going to cry a bit before and it's already going to help me with all of this development and not only that but if you also use the python SDK you are going to have some other goodies some other helper methods that are going to make your life a tiny bit more easier so

**13:04** · for example we are already shipping and I'm just putting this example because we have had a couple of questions around that today these metadata object also has some helpers to allow how to patch descriptions of a table how to patch the descriptions of columns so all of these little interactions we are already coding all of this logic and shipping it as part of the Python SDK but some question that many of you might

**13:35** · have here is okay this is good it's interesting I can create some of these standard language objects into the python site how can I make sure that the objects and this these definitions that I'm putting on the python side are actually going to match everything that's going on in the server that's a very good question and the answer is because we are centralizing

**14:00** · all of these definitions of the standard via Json schema and the good thing about the Json schema it's not only that it's super expressive so it allows us to put the names the types the descriptions constraints it allows us to put a bunch of things but it also has great tooling support so from this single repository

**14:21** · of Json schemas we can automatically generate the Java code that it's going to power up the server the python code that it's going to be the basis of the Python SDK also the typescript code that is the one helping us with building all the UI as well as how we are storing the data the metadata and the database and the documentation so if you are curious

**14:44** · and you want to learn a bit more about which tools we are actually using to make these Transformations you have all of the all of the links here many many thanks to the communities and the followers that are actually powering up these projects because those are super super helpful but going back to the Json schema topic this is how we are actually able to make sure that all of these different pieces of

**15:09** · open metadata all of these different uh parts of the architecture that are even developed in different languages are always staying up to date and able to talk to each other now closing the Json schema parenthesis

**15:28** · what are the props of creating a table with the python SDK what we were just saying we have this is a standard a half all of these validations in Python pycharm is going to cry BS code is going to cry if I'm just doing some mistakes here so we get all of these validations as well as what we were also seeing before all of these helper methods to make our lives a bit easier so maybe I don't want to interact just raw with an API we have

**15:56** · all of these utilities on top that help us create all of these uh all of these logic flow and what's the con that it's language specific you don't want to use python or you don't have and somewhere any python environmental job environment to run all of this logic 10 maybe you are better off by using directly the the API but

**16:20** · again this depends on your use cases this depends on the context of the solution that you are going to build using all of these all of these apis automations and now that we have done a bit this API Journey this journey through the abstractions from the raw API to this

**16:42** · python SDK powered by this uh Json schema now we are finally Landing into the ingestion framework and here I'd like to start by explaining a bit how we are actually organizing and defining the workflows that we run from open metadata

**17:01** · and this is true from the ones that you deploy from the UI or also from the little code Snippets that we share for you to run on your own orchestrators because in the end they all use the same underlying classes they all use the same workflow structure that it's based in getting The Source data connecting to the source extracting the metadata from them and kind of trying to understand what's going on and doing this translation into the open metadata standard then we

**17:33** · optionally can have some processing of that data that's actually what is going on in the profiler workflow here we connect and we extract the information about the tables and here is where we are actually running all of the metrics we are putting all of this extra logic from the data that we extracted before and finally we send the results of all

**17:55** · of these computations into somewhere which by default this synced this somewhere is the API and again this is what happens when we're talking about metadata ingestion and we're talking about lineage DVT profiler Data Insights elastic surgery index all of these is what happens in all of these steps now how this connects to creating this

**18:20** · custom connector the idea is that we don't need to focus we don't need to really care about how this data gets into the cell because we already have this abstraction we already have this logic flow on how the metadata gets

**18:37** · extracted and how the metadata then reaches the open metadata service the open metadata server so the main benefit of just creating this custom connector is that we are only going to be working on the part of the source we don't really care on how this information then gets flown internally step after step how the API call it is to send all of

**19:01** · these metadata objects into open metadata we don't really care about that we just need to focus on this first piece of here how do we extract the information from my internal systems and how do I do the transformation how do I to this translation from the metadata from The Source into the open metadata standard other goodies that come from here that this ingestion framework is actually

**19:29** · what we have very well embedded into the open metadata UI so while if you use the API or directly the the python SDK or the Java SDK you would need to find your own solution into hosting and running that code bit random script be it a CI CD process we

**19:50** · also like wrote about that uh a couple of weeks back on how you can actually use the python SDK to extract metadata from a custom ml model and send that to open metadata that would be a very good use case to use the python SDK because we have a cicd pipeline and you want that every time that you push an ml

**20:10** · model to plot you have the metadata updated that's a different use case than when we are talking with the custom connector here what we are bringing is this definition of the source is this a skeleton on how you can connect to a specific Source system in the company and when this gets integrated into the UI any open metadata admin can create

**20:32** · the ingestion pipelines can schedule them directly from there so you don't need to add any more whistles into the architecture you just play and Define how this extraction and translation of the metadata works and open metadata is going to be taking care of the rest

**20:53** · and this is basically the I just got a little bit excited and I didn't change this light that's basically the discussion that we were just having right the pros just focus on the logic Define what you need to Define forget about the rest the conus you don't have as much flexibility as if you were just playing with the API because you need to make sure that your pieces fit with the definitions that we have in the open metadata workflows

### Demo: Creating a Custom Connector

**21:21** · that being said let's just start with the demo let's do some action and let's hope that there is no more VMO FX aside from the internet breaking here so what we're going to do now it's we're just going to imagine specific use case when in our organization we have a process that creates a CSV with some

**21:43** · data in this case I didn't have much more imagination that creating a CSV that is defining the names The Columns and the types for a series of tables and what we're going to do what we're going to play with this custom connector is that we are going to read pcsv we are going to validate that the information in there exactly what we are expecting to get what we were seeing before we are going to translate this Source information into the open

**22:11** · metadata standard and finally we're just going to knock on the door on the next step on the workflow and just forget because this is going to happen automatically the process of okay now we have everything translated and how it reaches into the open metadata server the ingestion framework is going to take care for you if you want to follow this along either now with me or at your own pace whenever

**22:38** · you want we have all of this code that I'm going to show you in this open metadata demo repo we not only have this we have some demos on how to play with uh custom lineage files I think I had an

**22:53** · example with with Hive how you can also integrate with depositors for end tables how you can integrate with red panda we have a bunch of demos and examples in there so feel free to take a look and see if you can reduce some of these processes for specific needs that you have in either in your organization or in any

**23:14** · other project that you might be playing with so now I'm just going to jump here in the repo I'm just going to zoom in a little bit more and here what we're going to find are all of the necessary steps to make this running but but it's interesting it's that if we

**23:35** · just go here to the end and actually I'm just going to start on the end I'm just going to show you how everything looks like from open metadata and then we are just going to pull the thread a bit to understand what are the internals so that when the time comes from you to create your own custom connectors you already have some helpers you already have some Clues on where to start and what is it that you can customize here so to start with the ingestion I'm just coming into my own local open metadata

**24:08** · deployment as you can see I did a couple of tests before joining here and I'm going to click in this custom database connector I'm just going to give a name

**24:24** · click on next and this is going to ask me what's the source python class name we are saying that this is Gusto the ingestion framework does not know this implementation so we need a way to actually pass the class that the workflow is going to need to load in order to run in this case we have this listed here in the readme so I'm just going to be copying this information

**24:54** · and we do not only need to pass this information we can optionally add some other options some other variables that for us might be important to control in each of the custom services in this case I'm extracting database I am extracting data sorry from a CSV file so what will I need to pass where the test is CSV file leave so I have defined my custom connector to

**25:22** · accept two connection options one is going to be this Source directory so I'm just going to part to put this here and where the CSV really lives

**25:39** · and these other option here which is poorly fan of it a business unit for us to give a name I'm just going to say that the business unit is called sales and before I run these I want to show you how the CSV looks

**25:59** · like so this is the data that we're going to ingest that we're going to translate and that we're going to set into open metadata I'm going to expect to find a couple of tables named table one and table two each of them have their own columns and each of them have their own types and note how here I just followed this

**26:23** · convention quote unquote that the columns are going to be separated by semicolons that I'm going to have a column named column names and another column named column types all of these is just what makes sense for me in this

**26:38** · example it might be different for organization one it might be different for organization two it might be different from Organization three but the idea is that with these custom connectors we can make sure that the logic that makes sense in our context can be translated into this sources structure that we need for the ingesting framework Torah so before diving a bit more deeper into the code

**27:05** · is knocked me out sorry about that we just add this information again here real quick

**27:26** · Source directory and the sample CSV awesome going to save and I'm going to create an ingestion because this is a custom connector the ingestion framework knows how to create ingestions directly from the UI just going to leave all of the defaults no DBT to configure here and let it run every hour

**27:59** · when I look at the service it is already started running and it already finished as everything as we said it stayed together it can come here and I can check the logs right and I can come into my database view you see this business unit parameter that I sent it's going to be translated in this case in the database name why because I developed it in that

**28:25** · way it made sense for my use case so I can just add this information the way uh the way that I need here this scheme is going to be default and I'm just going to find my table 1 and table 2 with older columns and all

**28:42** · their types the CSV did not have any more information so there is no more information for me to pass and to translate so that's it but this is just a super tiny example on what we can eventually do by having more and more and more information that is supported by the by

**29:02** · the standard so if we know just jump a bit here I already have that open into the code in order for us to create this custom source this custom connector we just need to create a class that extends this Source right so this is the class used internally by the ingesting framework that it's going to be the one connecting into my source system doing the translation and calling this next record to keep iterating on everything that

**29:35** · needs to be fetched and sent into the next steps of the of the workflow now if we take a look this is my CSV connector implementation in my next record I'm doing different things first I'm creating the database service then I'm creating the database based on my business unit name then I'm creating the schema and finally I'm sending that data and all of this code here you see I'm creating a create table request this is

**30:06** · actually the same object that we were using here so ingesting framework completely powered by this python SDK so the same logic the same learning curve that you're going to be able then to reuse in your CI CD scripts is also going to help you into develop and build your own custom connectors here

**30:31** · then the final question before uh before we close this is how can I make the open metadata uh ingestion framework aware of this class and the best way to actually do that is to extend any of our open metadata

**30:53** · ingestion images and pass your python code link here so in this case I'm just passing the directory that contains all my files I'm passing the setup to install the package and passing the sample CSV for Simplicity and finally I'm installing the information so whenever I'm in the UI and I'll come into my service and I'll run this ingestion this is running on this container in which I have already sent the code that is required for me to run

**31:25** · this python Plus and that would be it for today on our side that would be it for the highlights that would be it for the demo thank you very very much to everyone for coming thank you for your attention if you have any questions any comments we have some time and this is for you so please don't be shy hi this is Diddy I have a question

**31:58** · um yeah so this is regarding the tag propagation say I have a tag at a parent object can that be propagated uh like automatically to all the children in the hierarchy

**32:15** · so if you want to pick up this one so uh this uh the one that um Pere is talking about this connectors right for collecting metadata from the sources and ingesting that into open metadata in terms of tag propagation now that our column lineage is uh getting you know more solid uh we have had it for a couple of releases we will start building you know tools which will automatically do that for you you don't need to write a connector right so so

**32:47** · the example that Perez is giving is how to ingest the metadata from various sources these ones are workflows that take the metadata that already exists in open metadata and then make use of it to do certain things in your case tag exists on Source table automatically it gets propagated into the destination tables destination columns these are some things that we will build it ourselves you would not need a separate connector but you know as uh Perez was

**33:14** · giving an example if you want to build it yourself you could also do it except that you will be connecting to open metadata and then you're writing back to you'll be writing back to open metadata okay so this functionality is something that will come later it doesn't exist today right it doesn't exist today there's a lot of automation that we have on our roadmap to build um tag propagation description propagation is one of them

**33:41** · okay what about the ownership I mean if I have an ownership say for example at a database level can that be propagated or that will also come in later so we have a right now in 0 to 13.2 if you set up uh ownership for the database schema level all the tables will inherit the ownership unless you change it right manually that is perfect okay yeah the problem that we were seeing was people keep adding new tables to the database schema right and these new tables don't have owners so now it inherits from its

**34:13** · higher you know uh from the hierarchy Above So database schema um you know owner is propagated to table database ownership is propagated to database schema and this is true for you know many hierarchical objects that we have in our system okay okay this was one of our requests and I think you guys have fulfilled that we added it because you know because of your input oh my God okay thank you so much I appreciate it

**34:45** · yeah just a shout out to open metadata team you guys have been awesome you know and supporting me and my team so I'm really very very thankful and we are actually using open metadata now it's official so it's very very uh you know great thanks to Suresh and Harsha and

**35:04** · DePere and all the people that who helped us with my like lots and lots of questions that keep coming up you know so super appreciated no I I think you know questions are very important for us uh also if you have future ideas if something is confusing the documentation is not clear together as a community you know with your feedback we can continuously improve this uh feel free to just provide us any feedback don't hold it back

**35:34** · you know I'm not holding back I'm giving you more feedback this is for you know even rest of the communities please follow me this uh uh footsteps provide us feedback any ideas you have

**35:52** · there's one thing from my side hi this is Laila from move and firstly about ready like to thanks the team Suresh Harsha and ayush and Teddy who are just being very supportive and constantly reply me for all my queries uh thank you again everyone for joining it was uh super awesome to see you folks so any questions that you have

**36:15** · just feel free to reach out in slack any ideas open up here if you have to request if you are brave enough open a PR we love seeing those so please don't keep anything to yourselves we're here to help and enjoy the rest of your day thank you everyone