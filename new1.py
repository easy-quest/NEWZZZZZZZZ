import sentry_sdk

def traces_sampler(sampling_context):
      # ...
      # return a number between 0 and 1 or a boolean

sentry_sdk.init(
    dsn="https://4bf745e65a994fd3b91c350709acf69c@o1044998.ingest.sentry.io/6020257",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # Alternatively, to control sampling dynamically
    traces_sampler=traces_sampler
)
