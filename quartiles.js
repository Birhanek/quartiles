

const asserting = require('assert')
class Quartiles{
    // constructor
    constructor(data){
        this.data = data
    }
    // sorting a given array of list in to ascending order
    ascendingOrder(){
        let value = 0
        for (let i=0; i<this.data.length; i++){
            for(let j=i+1; j<this.data.length; j++){
                
                if(this.data[i] >= this.data[j]){
                    value = this.data[i]
                    this.data[i] = this.data[j]
                    this.data[j] = value
                }
            }
        }
        return this.data
    }
    // finding the first quartile
    firstQuartile(data){
        
        let value = 0
        if(data.length %4 ===0){
            const  initial = data.length /4
            value = (data[initial] + data[initial+1])/2
            return value
        }
        else{
            value = data[Math.ceil(data.length/4)-1]
            return value
        }
        
    }
    // finding median also called the 2nd quartile
    median(data){
        let len = data.length
        if(len%2 === 0){
            const middle = len/2
            const value = (data[middle-1] + data[middle])/2
            return value
        }
        else{
            const value = data[(Math.ceil(len/2)-1)]
            return value
        }
    }
    // calculates the third quartile
    thirdQuartile(data){
        let value = 0
        if((data.length * 3) %4 ===0){
            const  initial = (data.length * 3) /4
            value = (data[initial] + data[initial+1])/2
            return value
        }
        else{
            value = data[Math.ceil((data.length * 3)/4)-1]
            return value
        }
    }
    // prints the range between the maximum and minimum values of the array or list
    rangeCalculator(data){
        let minimumValue = data[0]
        let maximumValue = 0
        let range =0

        for(let i=0; i<data.length; i++){
            if(data[i]>= maximumValue){
                maximumValue = data[i]
            }
            
        }
        for(let i=0; i<data.length; i++){
            if(data[i]<=minimumValue){
                minimumValue = data[i]
            }
        }

        range = maximumValue - minimumValue
        return range
    }
    // calculating the mean of a given data
    calculatingMean(data){
        let mean =0
        let sum = 0
        sum = data.reduce((preValue,nextValue)=>preValue + nextValue)

        mean = sum / data.length
        return mean
    }
    // calculating standard deviation
    standardDeviation(data){
        let value = this.calculatingMean(data)
        let sum = 0
        let variance = 0
       for(let i=0;i<data.length; i++){
            sum += (data[i]-value)**2
       }
       variance = sum / data.length

       return Math.sqrt(variance)


    }
    
}

// let us test our algorithm

const newData = new Quartiles([21,40,33,38,25,28,30])
const ascendingData = newData.ascendingOrder()
// ordered data
console.log(ascendingData)
// finding the First Quartile of a given list/array
const firstQuartile = newData.firstQuartile(ascendingData)
console.log(firstQuartile)
// finding the second Quartile of a given list/array
const secondQuartile = newData.median(ascendingData)
console.log(secondQuartile)
// finding the third Quartile of a given list/array
const thirdQuartile = newData.thirdQuartile(ascendingData)
console.log(thirdQuartile)

// printing the range between the maximum value and minimum value of the array
console.log(newData.rangeCalculator([102,83,99,92,71,40,65,84]))

// [102,83,99,92,71,40,65,84] [5,8,2,1,6,8]

// function roundToPrecision(num, precision){
//     let factor = Math.pow(10,precision)
//     return Math.round(num * factor) / factor
// }

//console.assert(asserting.strictEqual(roundToPrecision(newData.standardDeviation([5,8,2,1,6,8]),1),2.7,'true'))
