# Create a new subscription
subscription = client.subscriptions.create(client_id="uuid-of-client", price_id="price_123", plan="Premium")
print("Created Subscription:", subscription)

# Update a subscription
updated_subscription = client.subscriptions.update(
    subscription_id="uuid-of-subscription",
    new_price_id="price_456",
    new_plan="Basic"
)
print("Updated Subscription:", updated_subscription)

# Cancel a subscription
canceled_subscription = client.subscriptions.cancel(subscription_id="uuid-of-subscription")
print("Canceled Subscription:", canceled_subscription)
