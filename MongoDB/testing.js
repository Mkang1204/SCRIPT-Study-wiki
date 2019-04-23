-- not working
--Please connect to the M001 class Atlas cluster from the mongo shell or Compass and view the video.movies collection. How many movies match the following criteria?

--The cast includes either of the following actors: "Jack Nicholson", "John Huston".
--The viewerRating is greater than 7.
--The mpaaRating is "R".

{$and:{cast: {$exists: ["Jack Nicholson", "John Huston"]}},{viewerRating:{$gt: 7}},{mpaaRating:{$eq:'R'}};

right:
{cast: {$in: ["Jack Nicholson", "John Huston"]}, viewerRating: {$gt: 7}, mpaaRating: "R"}
