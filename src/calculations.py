function calculateRevenue(yieldAmount, sellingPricePerKg) {
  return yieldAmount * sellingPricePerKg;
}

function calculateTotalCost(costs) {
  return costs.reduce((total, cost) => total + cost.amount, 0);
}

function calculateProfit(revenue, totalCost) {
  return revenue - totalCost;
}

module.exports = {
  calculateRevenue,
  calculateTotalCost,
  calculateProfit,
};