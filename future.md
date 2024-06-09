Given more time, here's what I would do differently:

1. Webhook Configuration: Currently, I've set up a single webhook for all three event types. 
    While this approach is good enough for our current scale, I acknowledge its limitations. 
    If scalability were a concern, I would have created a separate webhook for each event type. 


2. Product Considerations: I came up with some product-related questions that require further discussion:

   * Team Event: When handling team events, I think it's nice to also deal with updating the team name.

   * Repository Deletion: I would discuss with Product whether it's important to them
   that the same person performs the creation and deletion.


3. Testing Strategy: I didn't write tests that mock the API call that the webhook creates,
I checked it manually. If I had more time, I would have done it.

4. Report Suspicious Users: It might be useful to keep track of the users who make suspicious actions for further
    investigation,