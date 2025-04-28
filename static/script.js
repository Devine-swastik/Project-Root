const diceElement = document.getElementById("dice");
const rollButton = document.getElementById("roll-button");

rollButton.addEventListener("click", async () => {
    // Step 1: Call the backend API to roll the dice
    const response = await fetch("/api/roll_dice");
    const data = await response.json();
    const diceValue = data.dice_value;

    // Step 2: Fetch the dice image from the backend
    const imageResponse = await fetch(`/api/dice_image/${diceValue}`);
    const blob = await imageResponse.blob();

    // Step 3: Create a URL for the image and display it
    const imageUrl = URL.createObjectURL(blob);
    diceElement.innerHTML = `<img src="${imageUrl}" alt="Dice ${diceValue}" style="width: 150px; height: 150px;">`;
});
