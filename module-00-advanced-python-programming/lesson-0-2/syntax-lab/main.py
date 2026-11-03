state = "queued"
attempts = 3
delay_seconds = 0.25
enabled = True
finished_at = None

print(state, type(state))
print(attempts, type(attempts))
print(delay_seconds, type(delay_seconds))
print(enabled, type(enabled))
print(finished_at, type(finished_at))

previous_attempts = attempts
attempts = attempts + 1
print("previous:", previous_attempts)
print("current:", attempts)

attempts = "four"
print(attempts, type(attempts))
