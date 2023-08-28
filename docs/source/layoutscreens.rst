Screens
=====

.. _layoutscreens:

Screen types
------------
PCN is composed of several screens that fall into two broad categories:

      **- Summary screens**
          These screens present the data that has been already entered and do not require any data entry by the user. :doc:`PatientRecord` and :doc:`EndOfVisit` are             two examples of Summary screens. An example of a summary screen can be seen below:
          
          .. image:: images/ChooseTreatment_VisitSummary.JPG
             :scale: 80 %
             
          
      **- Activity screens**
          These screens allow the user to enter data and record actions taken. These screens also provide necessary instructions to the user. Examples of such screens           are :doc:`ScoringScreen`, :doc:`TreatmentScreen` and :doc:`ActionScreen`. Below you can find an example of such a screen:
            
            .. image:: images/GeneralExam.JPG
             :scale: 80 %
            
            Since clubfoot can affect one or both the feet, PCN screens can be classified in another manner into:
            
            1. Screens which do not depend on the foot (i.e. left or right)
            Such screens do not have tabs (Right/Left). :doc:`GeneralExamScreen` and :doc:`AddNewVisit` screens are examples of such screens.
            
            2. Screens where the foot (i.e. left or right) matter
            Such screens have one or two tabs labelled Right and Left which can be used to switch to the appropriate foot. In unilateral clubfoot case many of such                 screens have only one tab. Many of such screens will have Continue to Left Foot Button instead of the Save button on loading. Whenever such a button shows             up, it is mandatory for the user to press it once before the Save button becomes active. Pressing the Continue to Left Foot changes the view from the Right             to the Left foot for that screen. Examples of such screens are :doc:`TreatmentScreen` and :doc:`EndOfVisit`. Below you can find an example of such a screen:
            
            .. image:: images/ClubfootHistory_1.JPG
             :scale: 80 %

Fields
----------
Activity/Data Entry screens are composed of fields that allow data entry/editing. Fields can be classified based on following criteria

1. Mandatory vs Optional
2. Data Type
3. Free Text vs multiple choice
4. Structured vs unstructured

There are different types of buttons/fields that PCN uses to gather information. 
     - Round buttons: a list of options where only one option can be selected
     - Square buttons: a list of options where multiple options can be selected
     - Drop-down menu: a list of options in a menu that unfolds when you click on it, where one option can be selected

Overview of the screens
-----------
In this part of the manual, different screens from PCN are explained step-by-step.
There are several screens that you might be interested in:

     - Different types of activity screens

           - :doc:`LogInScreen`
           - :doc:`AddNewPatient`
           - :doc:`GeneralHistoryScreen`
           - :doc:`ClubfootHistoryScreen`
           - :doc:`GeneralExamScreen`
           - :doc:`ClubfootExamScreen`
           - :doc:`ObservationScreen`
           - :doc:`ScoringScreen`
           - :doc:`TreatmentScreen`
           - :doc:`ActionScreen`
           - :doc:`AddNewVisit`
   
   - Different types of summary screens
   
          - :doc:`PatientRecord`
          - :doc:`EndOfVisit`
          - :doc:`ReportScreen`
   
   
