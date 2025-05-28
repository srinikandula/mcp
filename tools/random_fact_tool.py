def register_random_fact_tool(mcp):
    import random

    @mcp.tool()
    def random_fact_tool() -> str:
        """
        Returns a random fun fact.
        """
        facts = [
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries are not.",
            "Wombats poop cubes.",
            "Honey never spoils.",
            "Sharks are older than trees."
        ]
        return random.choice(facts)

