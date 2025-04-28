const diceBlock = document.getElementById("dice-block");
const rollButton = document.getElementById("roll-button");

rollButton.addEventListener("click", async () => {
    // Fetch random dice value from the backend
    const response = await fetch("/api/roll_dice");
    const data = await response.json();
    const diceValue = data.dice_value;

    // Update the dice block with the rolled number
    diceBlock.textContent = diceValue;
});
