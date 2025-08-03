import pandas as pd

# Load the dataset
df = pd.read_excel("Kigali_Wedding_Venues_Custom.xlsx")


# Preview the data
print(" Data Loaded")
print(df.head())
print("\n Dataset shape:", df.shape)
print("\n Data types:\n", df.dtypes)
# Convert Excel-style numbers to real dates
df["Booking_Date"] = pd.to_datetime(df["Booking_Date"], origin='1899-12-30', unit='D')

# Preview again
print("\n Booking Dates (Fixed):")
print(df[["Venue_Name", "Booking_Date", "Status"]].head())
#Total Venues, Unique Locations
print("🏢 Total Venues:", df["Venue_Name"].nunique())
print("📍 Locations:", df["Location"].unique())
#Bookings Per Status (Booked vs Available)
print("\n📊 Booking Status Count:")
print(df["Status"].value_counts())
#Most Booked Venues
print("\n🔥 Most Booked Venues:")
print(df[df["Status"] == "Booked"]["Venue_Name"].value_counts())
# Average Price by Location
print("\n💰 Average Price by Location:")
print(df.groupby("Location")["Price_(Frw)"].mean())
#Peak Booking Dates
print("\n📅 Most Popular Booking Dates:")
print(df["Booking_Date"].value_counts().head(5))
#Plot booking status
import matplotlib.pyplot as plt

df["Status"].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title("Booking Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.show()
# Check for Missing Values
print("🔍 Missing Values Check:")
print(df.isnull().sum())
#Check for Duplicates
print("\n📑 Duplicate Rows:", df.duplicated().sum())
#Check for Inconsistent Casing (e.g., venue/status)
df["Venue_Name"] = df["Venue_Name"].str.title().str.strip()
df["Status"] = df["Status"].str.capitalize().str.strip()
#Final Dataset Info After Cleaning
print("\n✅ Cleaned Dataset Shape:", df.shape)
print(df.head())
#Booking status plotting
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='Status', palette='pastel')
plt.title("Booking Status Distribution")
plt.show()
#Average price per location
avg_price = df.groupby('Location')['Price_(Frw)'].mean().reset_index()

sns.barplot(data=avg_price, x='Location', y='Price_(Frw)', palette='viridis')
plt.title("Average Price per Location")
plt.ylabel("Price (Frw)")
plt.show()


