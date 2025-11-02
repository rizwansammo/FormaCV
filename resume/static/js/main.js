document.addEventListener("click", (e) => {
  if (e.target.matches("[data-open='edu']"))
    document.getElementById("modal-edu").classList.remove("hidden");
  if (e.target.matches("[data-open='exp']"))
    document.getElementById("modal-exp").classList.remove("hidden");
  if (e.target.matches("[data-open='pro']"))
    document.getElementById("modal-pro").classList.remove("hidden");
  if (e.target.matches("[data-close='edu']"))
    document.getElementById("modal-edu").classList.add("hidden");
  if (e.target.matches("[data-close='exp']"))
    document.getElementById("modal-exp").classList.add("hidden");
  if (e.target.matches("[data-close='pro']"))
    document.getElementById("modal-pro").classList.add("hidden");
});
