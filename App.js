import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";

export default function App() {
  const [activity, setActivity] = useState("");
  const [value, setValue] = useState("");
  const [result, setResult] = useState("");

  const calculateFootprint = async () => {
    try {
      const response = await fetch("http://192.168.1.3:8000/calculate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: "User",
          email: "user@example.com",
          activities: [{ activity_type: activity, value: parseFloat(value) }],
        }),
      });
      const data = await response.json();
      setResult(data.total_emissions);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Carbon Footprint Tracker</Text>
      <TextInput
        style={styles.input}
        placeholder="Activity (e.g., car, bus)"
        onChangeText={(text) => setActivity(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="Value (e.g., km, kWh)"
        keyboardType="numeric"
        onChangeText={(text) => setValue(text)}
      />
      <Button title="Calculate" onPress={calculateFootprint} />
      {result ? <Text style={styles.result}>Emissions: {result} kg CO2</Text> : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", padding: 16 },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 16 },
  input: { borderWidth: 1, padding: 8, marginBottom: 8 },
  result: { fontSize: 18, marginTop: 16 },
});
