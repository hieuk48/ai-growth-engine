from typing import Optional, Dict, Any
import threading

# Simulated persistent storage for user call counts (replace with real DB in production)
_user_call_counts = {}
_user_call_counts_lock = threading.Lock()

# Simulated function to send upsell notification (replace with real implementation)
def send_upsell_notification(user_id: str) -> None:
    # In production, trigger email, in-app message, etc.
    print(f"[UPS ELL] User {user_id} reached 5 free calls. Triggering upsell.")

def get_user_call_count(user_id: str) -> int:
    with _user_call_counts_lock:
        return _user_call_counts.get(user_id, 0)

def increment_user_call_count(user_id: str) -> int:
    with _user_call_counts_lock:
        count = _user_call_counts.get(user_id, 0) + 1
        _user_call_counts[user_id] = count
        return count

def reset_user_call_count(user_id: str) -> None:
    with _user_call_counts_lock:
        _user_call_counts[user_id] = 0

def handle_free_call(user_id: str, call_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Handle a free API call for a user, trigger upsell after 5th call.

    Args:
        user_id (str): The unique user identifier.
        call_context (dict, optional): Additional context for the call.

    Returns:
        dict: Result with call count and upsell status.
    """
    call_count = increment_user_call_count(user_id)
    upsell_triggered = False

    if call_count == 5:
        send_upsell_notification(user_id)
        upsell_triggered = True

    return {
        "user_id": user_id,
        "call_count": call_count,
        "upsell_triggered": upsell_triggered
    }

# Example testable usage
if __name__ == "__main__":
    test_user = "user_123"
    for i in range(7):
        result = handle_free_call(test_user)
        print(f"Call {i+1}: {result}")