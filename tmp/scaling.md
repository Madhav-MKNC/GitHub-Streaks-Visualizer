# For vast amount of users we do:

- Caching: These services often use caching extensively. Data that doesn't change frequently, like a user's streak statistics, can be cached. Cached data can be quickly served to users without repeatedly hitting the API or database. This reduces the load on the server and improves response times.

- Scheduled Updates: Many services update data on a schedule. For example, GitHub streak data can be updated daily, weekly, or at some other regular interval using automation tools like GitHub Actions or cron jobs. This avoids the need to fetch data for every user in real-time when someone visits a user's profile.

- API Rate Limiting: API providers like GitHub impose rate limits to prevent abuse. Services that rely on external APIs must manage these rate limits efficiently. They might use token pools or queues to distribute API requests evenly and avoid hitting rate limits.
