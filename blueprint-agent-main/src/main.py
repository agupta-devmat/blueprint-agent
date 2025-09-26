import random
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.bedrock import BedrockConverseModel
from pydantic_ai.providers.bedrock import BedrockProvider
import logging

logging.basicConfig(level=logging.DEBUG)

AWS_REGION = "eu-central-1"


def get_random_roulette_number():
    """get a random roulette wheel number"""
    return random.randint(0, 36)


model = BedrockConverseModel(
    "eu.amazon.nova-micro-v1:0",
    provider=BedrockProvider(
        region_name=AWS_REGION,
    ),
)

roulette_agent = Agent(
    model=model,
    deps_type=int,
    system_prompt=(
        "Use the `roulette_wheel`function to see if the "
        "customer has won based on the number they provide."
    ),
)


@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> bool:
    """check if the square is a winner"""
    ctx.deps = get_random_roulette_number()
    print(f"square: {square}")
    print(f"ctx.deps: {ctx.deps}")
    return "winner" if square == ctx.deps else "loser"


app = roulette_agent.to_a2a()
