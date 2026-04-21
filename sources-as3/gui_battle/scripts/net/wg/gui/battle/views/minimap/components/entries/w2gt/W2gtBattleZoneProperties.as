package net.wg.gui.battle.views.minimap.components.entries.w2gt
{
   public class W2gtBattleZoneProperties
   {
       
      
      public var fillColor:int = 0;
      
      public var fillAlpha:Number = 0;
      
      public var fillBlendMode:String = null;
      
      public var outlineStyle:String = null;
      
      public var outlineThickness:Number = 0;
      
      public var outlineColor:int = 0;
      
      public var outlineAlpha:Number = 0;
      
      public var dotRadius:Number = 0;
      
      public var dotGap:Number = 0;
      
      public var outlineBlendMode:String = null;
      
      public var dotStep:Number = 0;
      
      public function W2gtBattleZoneProperties(param1:int, param2:Number, param3:String, param4:String, param5:Number, param6:int, param7:Number, param8:Number, param9:Number, param10:String)
      {
         super();
         this.fillColor = param1;
         this.fillAlpha = param2;
         this.outlineStyle = !!OUTLINE_STYLE.isIn(param4) ? param4 : OUTLINE_STYLE.SOLID;
         this.outlineThickness = param5;
         this.outlineColor = param6;
         this.outlineAlpha = param7;
         this.dotRadius = param8;
         this.dotGap = param9;
         this.dotStep = param8 * 2 + this.dotGap;
         this.fillBlendMode = param3;
         this.outlineBlendMode = param10;
      }
      
      public function get isSolid() : Boolean
      {
         return this.outlineStyle == OUTLINE_STYLE.SOLID;
      }
      
      public function get isDotted() : Boolean
      {
         return this.outlineStyle == OUTLINE_STYLE.DOTTED;
      }
   }
}

class OUTLINE_STYLE
{
   
   public static const SOLID:String = "solid";
   
   public static const DOTTED:String = "dotted";
   
   public static const ALL:Array = [SOLID,DOTTED];
    
   
   function OUTLINE_STYLE()
   {
      super();
   }
   
   public static function isIn(param1:String) : Boolean
   {
      return ALL.indexOf(param1) >= 0;
   }
}
