{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c6f3dbe1-99d5-4ca5-bef6-31278386c996",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Module 2: Individual Programming Assignment 1\n",
    "\n",
    "Useful Business Calculations\n",
    "\n",
    "This assignment covers your basic proficiency with Python.\n",
    "'''\n",
    "\n",
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''Savings.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "    \n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    return(int(gross_pay * tax_rate) - expenses)\n",
    "\n",
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    '''Material Waste.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates how much material input will be wasted\n",
    "        after running a certain number of jobs that consume\n",
    "        a set amount of material.\n",
    "\n",
    "    To get the waste of a set of jobs:\n",
    "        1. Multiply the number of jobs by the material consumption per job.\n",
    "        2. Subtract the total material consumed from the total material available.\n",
    "\n",
    "    The users of this function also want you to format the output as a string, annotated with the\n",
    "        units in which the material is expressed. Do not add a space between the number and the unit.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    total_material: int\n",
    "        the total material available\n",
    "    material_units: str\n",
    "        the units used to express a quantity of the material (e.g., \"kg\", \"L\", etc.)\n",
    "    num_jobs: int\n",
    "        the number of jobs to run\n",
    "    job_consumption: int\n",
    "        the amount of material consumed per job\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    str\n",
    "        the amount of remaining material expressed with its unit (e.g., \"10kg\").\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    return(\"%s%s\" % ((num_jobs * job_consumption)-(total_material),(material_units)))\n",
    "\n",
    "def interest(principal, rate, periods):\n",
    "    '''Interest.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the final value of an investment after\n",
    "        gaining simple interest over a number of periods.\n",
    "\n",
    "    To calculate simple interest, simply multiply the principal to the quantity (rate * time). \n",
    "        Add this amount to the principal to get the final value.\n",
    "\n",
    "    Round down the final amount.\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    principal: int\n",
    "        the principal (i.e., starting) amount invested, expressed in centavos\n",
    "    rate: float\n",
    "        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)\n",
    "    periods: int\n",
    "        the number of periods invested\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the final value of the investment\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    return(int(principal*(rate*periods)))\n",
    "\n",
    "def body_mass_index(weight, height):\n",
    "    '''Body Mass Index.\n",
    "    5 points.\n",
    "\n",
    "    This function calculates the body mass index (BMI) of a person\n",
    "        given their weight and height.\n",
    "\n",
    "    The formula for BMI is: kg / (m ^ 2)\n",
    "        (i.e., kilograms over meters squared)\n",
    "\n",
    "    Unfortunately, the users of this function use the imperial system.\n",
    "        You will need to first convert their arguments to the metric system.\n",
    "    \n",
    "    Parameters\n",
    "    ----------\n",
    "    weight: float\n",
    "        the weight of the person, in pounds\n",
    "    height: list\n",
    "        the height of the person, expressed as a list of two integers.\n",
    "        the first integer is the foot component of their height.\n",
    "        the second integer is the inches component of their height.\n",
    "        for example, 5'10\" would be passed as [5, 10].\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    float\n",
    "        the BMI of the person.\n",
    "    '''\n",
    "    # Replace `pass` with your code. \n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    height_ft = height[0]\n",
    "    height_in = height[1]\n",
    "    height = [height_ft,height_in]\n",
    "    return(float(((weight/2.205) / (((height_ft*0.3048 + (height_in*0.0254)) ** 2)))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9cb6ca5d-5a59-4660-8bd8-fa9d96b5fbef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "699"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "savings(10_000, 0.57, 5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "db8ce076-dd60-4851-ab36-d10bcda216b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'400L'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "material_waste(100,\"L\",50,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b8a720f8-2dda-44b0-b0f6-fd6cff7c1c13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1500"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "interest(10_000,0.03,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1143f32d-60cd-4d7d-8727-9c09c953ea24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25.720176359325414"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "body_mass_index(174.2,[5,9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b1d3d52-1d6c-44eb-b04a-e2dcdf865a5c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
